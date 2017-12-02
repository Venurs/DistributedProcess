"""
分布式进程
master
"""


from multiprocessing.managers import BaseManager
import queue
import random





def result_fun(list_result):
    for res in list_result:
        print(res)


#  设置任务队列和接收返回结果的队列
task_queue = queue.Queue()
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':

    #  将队列注册到网络BaseManager.register
    BaseManager.register("get_task_queue", callable=return_task_queue)
    BaseManager.register("get_result_queue", callable=return_result_queue)
    #  绑定端口 BaseManager()
    m = BaseManager(address=("", 5000), authkey=b"1234")
    #  启动队列
    m.start()
    #  获得网络访问对象
    task = m.get_task_queue()
    result = m.get_result_queue()
    #  放任务到task_queue
    list_result = []
    task.put(list_result)
    print("试图获取执行结果中。。。")
    #  接收任务执行结果到result_queue
    list_result = result.get(timeout=10)
    result_fun(list_result)
    print('Try get results...')
    #  关闭
    m.shutdown()
    print("master执行完毕")


