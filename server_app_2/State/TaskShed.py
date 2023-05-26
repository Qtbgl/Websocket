import asyncio


class TaskShed:
    tran_task: asyncio.Task = None

    def load_task(self, where, coro_obj):
        if self.tran_task:
            b = not self.tran_task.done()
            if b and not self.tran_task.cancelled():
                print(f'({where}) load_task 警告：已存在任务，且未结束：', self.tran_task)

        task = asyncio.get_running_loop().create_task(coro_obj)
        self.tran_task = task

    def trans_cancel(self, where):
        if self.tran_task is None:
            print(f'({where}) trans_cancel 警告：任务未存储')

        if self.tran_task.done():
            print(f'({where}) trans_cancel 警告：任务已结束')

        if self.tran_task.cancelled():
            print(f'({where}) trans_cancel 警告：任务已取消')

        if not self.tran_task.cancel():
            print(f'({where}) trans_cancel 警告：任务取消失败')
