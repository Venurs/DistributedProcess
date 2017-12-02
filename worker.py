"""
分布式进程
worker
"""

import time
import random
from multiprocessing.managers import BaseManager


def task_fun(list1):
    print("任务执行中。。。")
    for i in range(1, 20):
        num = random.randint(1, 10000)
        list1.append(num)
        print("将%d添加到链表末尾" % num)
    return list1


#  注册
BaseManager.register("get_task_queue")
BaseManager.register("get_result_queue")
#  链接服务器，包括IP和端口，口令
server_ip = ""
w = BaseManager(address=(server_ip, 5000), authkey=b"1234")
w.connect()
#  获取对象
task = w.get_task_queue()
result = w.get_result_queue()
# task取任务
list_task = task_fun(task.get(timeout=5))
# result放入执行结果
result.put(list_task)

print("worker 执行完毕。。。")





