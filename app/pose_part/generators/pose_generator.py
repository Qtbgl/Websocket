from app.pose_part.Frame.AnimFrame import anim_pose
from app.pose_part.Frame.PoseData import PoseData, UEQuat
from app.pose_part.generators.blazepose_generator import blazepose_generator
from app.pose_part.solve.BodyPoint import BodyPoint
from app.pose_part.solve.BoneRotate import BoneRotate


def pose_generator(video):
    try:
        for bz, seq, sec in blazepose_generator(video):
            print('(pose generator) 生成', seq)
            lwm = bz.pose_world_landmarks.landmark
            ue_x = [each.x for each in lwm]
            ue_y = [-each.z for each in lwm]
            ue_z = [-each.y for each in lwm]
            bp = BodyPoint(ue_x, ue_y, ue_z)
            br = BoneRotate(bp)
            # 数据处理
            pose = PoseData()
            pose.upperarm_l = UEQuat(br.l_upperarm.as_quat())
            pose.lowerarm_l = UEQuat(br.l_lowerarm.as_quat())

            am = anim_pose(pose, seq, sec)
            yield am

    except Exception as e:
        print('(pose generator) 捕获并传递异常：', type(e), e)
        raise e
    finally:
        print('(pose generator) 生成器结束')
