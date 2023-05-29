import cv2
import mediapipe as mp

from app.utils.Excepts import VideoCaptureFailed, ImgProcessExc


def blazepose_generator(video):
    print('(blazepose generator) 尝试读取视频：', video)
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print('(blazepose generator) 抛出异常 VideoCaptureFailed：打开时')
        raise VideoCaptureFailed(on_open=True)

    try:  # 正常打开视频
        fps = cap.get(cv2.CAP_PROP_FPS)
        delta = 1 / fps
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        print('(blazepose generator) 正在生成 mediapipe.solutions.pose')
        mp_pose = mp.solutions.pose
        with mp_pose.Pose(
                static_image_mode=False,
                min_detection_confidence=0.5) as pose:
            sec = 0
            for i_frame in range(frame_count):
                if not cap.isOpened():
                    raise VideoCaptureFailed(on_open=False)
                ret, frame = cap.read()

                # ret，正确读取 True，BGR 图像：frame.shape = (640,480,3)
                if not ret:
                    raise VideoCaptureFailed(on_open=False)
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                sec += delta
                yield pose.process(image), i_frame + 1, sec
    except VideoCaptureFailed:
        print('(blazepose generator) 抛出异常 VideoCaptureFailed：读取时')
        raise

    except Exception as e:
        print('(blazepose generator) 捕获并转化异常：', type(e), e)
        raise ImgProcessExc

    finally:
        print('(blazepose generator) 退出关闭 VideoCapture：', cap)
        cap.release()
