import websockets
import asyncio
import threading
import json
import time


# Server类
class MyServer:
    """
    private的部分，内部过程随便看看：
        init()：定义了类的成员变量
        consumer_handler()：执行consumer()，解析收到的消息
        producer_handler()：执行producer()获得要发送的消息，再执行send()发送消息
        handler()：管理消费者和生产者
        consumer()：解析收到的消息，现在只打印出来，并把isExecute=True
        producer()：遍历listcmd列表，pop首元素
        connect()：连接
        add_cmd()：接收输入，做成json字符串，保存在listcmd中

    public的部分，用这里的就行了：
        start_server()：开启服务并等待连接
        stop_server()：关闭服务
        send_time()：发送时间
    """

    # private
    def __init__(self, host='127.0.0.1', port='23333'):
        self.__host = host  # ip
        self.__port = port  # 端口号
        self.__listcmd = []  # 要发送的信息的列表
        self.__server = None
        self.__isExecute = False  # 是否执行完了上一条指令
        self.__message_value = None  # client返回消息的value

    def __del__(self):
        self.stop_server()

    async def __consumer_handler(self, websocket, path):
        async for message in websocket:
            # await asyncio.sleep(0.001)
            await self.__consumer(message)

    async def __producer_handler(self, websocket, path):
        while True:
            await asyncio.sleep(0.000001)
            message = await self.__producer()
            if message:
                await websocket.send(message)

    async def __handler(self, websocket, path):
        consumer_task = asyncio.ensure_future(self.__consumer_handler(websocket, path))
        producer_task = asyncio.ensure_future(self.__producer_handler(websocket, path))
        done, pending = await asyncio.wait([consumer_task, producer_task], return_when=asyncio.FIRST_COMPLETED, )
        for task in pending:
            task.cancel()

    # 接收处理
    async def __consumer(self, message):
        print('recv message: {0}'.format(message))
        self.__isExecute = True
        # jsonContent=json.loads(message)
        # self.__isExecute=jsonContent['IsExecute']
        # self.__message_value=jsonContent['Value']

    # 发送处理
    async def __producer(self):
        if len(self.__listcmd) > 0:
            return self.__listcmd.pop(0)
        else:
            return None

    # 创建server
    def __connect(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        print('start connect')
        self.__isExecute = True
        if self.__server:
            print('server already exist')
            return
        self.__server = websockets.serve(self.__handler, self.__host, self.__port)
        asyncio.get_event_loop().run_until_complete(self.__server)
        asyncio.get_event_loop().run_forever()

    # 往要发送的命令列表中，添加命令
    def __add_cmd(self, topic, key, value=None):
        self.__message_value = None
        while not self.__isExecute:  # 没有收到处理
            pass
        content = {'Topic': topic, 'Data': {'Key': key, 'Value': value}}
        jsonObj = json.dumps(content)
        self.__listcmd.append(jsonObj)
        print('add cmd: {0}'.format(content))
        self.__isExecute = False

    # public
    # 开启服务
    def start_server(self):
        print('start server at {0}:{1}'.format(self.__host, self.__port))
        t = threading.Thread(target=self.__connect)
        t.start()

    # 关闭服务
    def stop_server(self):
        print('stop server at {0}:{1}'.format(self.__host, self.__port))
        if self.__server is None:
            return
        self.__server.ws_server.close()
        self.__server = None

    # 发送时间
    def send_time(self):
        self.__add_cmd('Unreal', 'Time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
