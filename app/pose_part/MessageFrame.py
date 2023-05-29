import json


class MessageFrame:
    msg: str

    def __init__(self):
        self.on_error = False  # 任何出错
        self.on_anim = False

    def json_str(self):
        try:
            return json.dumps(self.json_dict())
        except TypeError as e:
            feedback = f'发送格式出错：{e}'
            print(feedback)
            return msg_error(msg=feedback)
            
    def json_dict(self):
        D = self.__dict__
        return D


def msg_error(msg):
    mf = MessageFrame()
    mf.msg = msg
    mf.on_error = True
    return json.dumps(mf.json_dict())
