import json


class ToJsonStr:
    def json_str(self):
        try:
            return json.dumps(self.json_dict())
        except TypeError as e:
            print('json_str 解析异常：', e)
            return json.dumps(None)

    def json_dict(self):
        D = self.__dict__
        for k in D:
            if isinstance(D[k], ToJsonStr):  # 传递调用属性方法，使其变成字典
                D[k] = D[k].json_dict()

        return D
