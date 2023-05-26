from server_app_2.State.MyState import MyState
from server_app_2.State.TaskShed import TaskShed
from server_app_2.utils.Excepts import ConnQuit
from server_app_2.utils.MessageParser.IdleDecide import IdleDecide
from server_app_2.utils.MessageParser.TransDecide import TransDecide


class GameState(MyState):
    shed: TaskShed = TaskShed()

    def idle_deal(self, message):
        info = IdleDecide()
        if info.fit(message):
            if info.msg:
                print('(IDLE) 接收到消息: ', info.msg)

            if info.to_transmit:
                self.shed.load_task('IDLE', self.transmit())
                self.state_i = 1

            if info.to_quit_conn:
                raise ConnQuit

    def tran_deal(self, message):
        info = TransDecide()
        if info.fit(message):
            if info.msg:
                print('(TRANSMIT) 接收到消息: ', info.msg)

            if info.to_quit_tran:
                self.shed.trans_cancel('TRANSMIT')
                self.state_i = 0

            if info.to_quit_conn:
                self.shed.trans_cancel('TRANSMIT')
                raise ConnQuit
