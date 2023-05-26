import json
from json import JSONDecodeError

from app.utils.Excepts import MsgNotFit
from app.utils.Context.RecvFits import RecvFits


class RecvDecide:
    msg: str
    decide: int

    def _decide_fit(self, obj, decide):
        pass

    def fit(self, message: str) -> bool:
        with RecvFits(self.__class__.__name__) as test:
            obj = fit_json_object(message)
            self.msg = obj.get('msg')
            self.decide = obj.get('decide')
            self._decide_fit(obj, self.decide)

        return not test.is_failed


def fit_json_object(message):
    try:
        obj = json.loads(message)
    except JSONDecodeError:
        raise MsgNotFit('json fail to decode message: ' + message)

    if isinstance(obj, dict):
        return obj
    else:
        raise MsgNotFit('input is not a object: ' + message)
