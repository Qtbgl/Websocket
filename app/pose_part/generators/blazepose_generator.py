import cv2
import mediapipe as mp


def blazepose_generator(video):
    try:
        cap = cv2.VideoCapture(video)
        fps = cap.get(cv2.CAP_PROP_FPS)
        delta = 1 / fps
        sec = 0
        mp_pose = mp.solutions.pose
        with mp_pose.Pose(
                static_image_mode=False,
                min_detection_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()  # ret，正确读取 True，BGR 图像：frame.shape = (640,480,3)
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                sec += delta
                yield pose.process(image), sec
    finally:
        cap.release()
