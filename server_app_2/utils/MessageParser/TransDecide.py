from server_app_2.utils.Excepts import MsgNotFit
from server_app_2.utils.MessageParser.RecvDecide import RecvDecide


class TransDecide(RecvDecide):
    to_quit_conn = False
    to_quit_tran = False

    def _decide_fit(self, obj, decide):
        if self.decide == 1:
            self.to_quit_tran = True
        elif self.decide == 2:
            self.to_quit_conn = True
        elif self.decide is not None:
            raise MsgNotFit(f'the decide of input is ignored: {decide}')  # 过滤 3
