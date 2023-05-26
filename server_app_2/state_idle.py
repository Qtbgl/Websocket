from server_app_2.utils.Excepts import MsgNotFit, ConnQuit
from server_app_2.utils.RecvDecide import RecvDecide


async def state_idle(websocket):
    async for message in websocket:
        info = IdleDecide()
        if info.fit(message):
            if info.msg:
                print('(IDLE) 接收到消息: ', info.msg)

            if info.to_transmit:
                return

            if info.to_quit_conn:
                raise ConnQuit


class IdleDecide(RecvDecide):
    video: str
    # 决策结果以下
    to_quit_conn = False
    to_transmit = False

    def _decide_fit(self, obj, decide):
        self.video = obj.get('video')
        if decide == 1:  # 进行决策
            self.to_transmit = True
        elif decide == 2:
            self.to_quit_conn = True
        elif decide is not None:
            raise MsgNotFit(f'the decide of input is ignored: {decide}')  # 过滤 3

        if self.to_transmit:
            if self.video is None:
                raise MsgNotFit('the video of input is not found')  # 过滤 4
