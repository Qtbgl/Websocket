class A:
    def __enter__(self):
        print('创建 + 初始化')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('关闭进入')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('关闭进出')
        return False


c = A()
print(c)
with c:
    print(111)
    raise KeyError('???')
    print(222)
