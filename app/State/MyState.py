import asyncio
import websockets

from app.pose_part.Frame.AnimFrame import anim_end, anim_cancelled
from app.pose_part.FrameSourceChoose import FrameSourceChoose
from app.utils.Excepts import VideoCaptureFailed, ImgProcessExc


class MyState:
    def __init__(self, websocket):
        self.websocket = websocket
        self.state_i = 0
        self.frameSource = FrameSourceChoose(from_simulate=False)  # 在创建时才 import模型

    def state_deal(self, message):
        if self.state_i == 0:
            self.idle_deal(message)
        else:
            self.tran_deal(message)

    def idle_deal(self, message):
        pass

    def tran_deal(self, message):
        pass

    async def transmit(self, video):
        try:
            for frame in self.frameSource(video):  # TODO
                await self.websocket.send(frame)  # debug - 程序连接直接关闭后会卡在这里
                await asyncio.sleep(0.000001)

            await self.websocket.send(anim_end())
        except VideoCaptureFailed:
            await self.websocket.send(anim_cancelled(msg=f'读取视频失败："{video}"'))
        except ImgProcessExc:
            await self.websocket.send(anim_cancelled(msg=f'图像处理异常，视频："{video}"'))
        except asyncio.CancelledError:
            print('(TRANSMIT) : 动画生成任务取消')
        except websockets.ConnectionClosedOK:
            print('(TRANSMIT) : 动画生成终止：连接关闭OK')
        except websockets.ConnectionClosed:
            print('(TRANSMIT) : 动画生成终止：连接异常关闭')
        except Exception as e:
            print("(TRANSMIT) : 捕获残余异常：", type(e), e)
        finally:
            print('(TRANSMIT) 任务结束或取消')
            self.state_i = 0  # 任务结束或取消，改回标志位
