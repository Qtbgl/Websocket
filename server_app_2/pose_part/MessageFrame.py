import json


class MessageFrame:
    msg: str
    on_error = False  # 任何出错
    on_anim = False

    def json_str(self):
        try:
            return json.dumps(self.__dict__)
        except TypeError as e:
            feedback = f'发送格式出错：{e}'
            print(feedback)
            return msg_error(msg=feedback)


def msg_error(msg):
    mf = MessageFrame()
    mf.msg = msg
    mf.on_error = True
    return json.dumps(mf)
