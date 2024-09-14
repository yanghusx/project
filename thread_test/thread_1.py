import threading
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time
import os

import shutil


def func(name, t):
    while True:
        time.sleep(t)
        return ("t_id:%s, name: %s" % (threading.get_ident(), name))

class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self) -> None:
        for i in range(100):
            print("i: %s, name:%s" % (i, self.name))


def read_result(res):
    print(">>>:%s" % res.result())

def get_dir_content(path=None):
    """
    获取目录下的所有文件
    :param path: 路径
    :return: 返回一个列表，包含所有的文件名
    """
    # file_list = []
    # for root, dirs, files in os.walk(path):
    g = os.walk("D:\\\project\\new")
    for path, dir_list, filer_list in g:
        print("<<<<<<<<<<<<<<")
        for dir_name in dir_list:
            print(os.path.join(path, dir_name))
        print("<<<<<<<<<<<<<<")
        print("++++++++++++++")
        for filer_name in filer_list:
            print(os.path.join(path, filer_name))
        print("++++++++++++++")

class myClassTest(object):
    def __init__(self, name):
        self.name = name
    @classmethod
    def func(cls):
        print("Name: %s"% "迭代")
if __name__ == '__main__':
    # t1 = Thread(target=func, args=("周",))
    # print(12222)
    # time.sleep(2000)
    # t2 = Thread(target=func, args=("张",))
    # t3 = Thread(target=func, args=("刘",))
    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()

    # 面向对象
    # p1 = MyThread("周")
    # p2 = MyThread("王")
    # p3 = MyThread("k")
    # p1.start()
    # p2.start()
    # p3.start()

    # with ThreadPoolExecutor(2) as t:
    #
    #     for i in range(3):
    #         t.submit(func, "周",2).add_done_callback(read_result)
    #         t.submit(func, "zhang", 3).add_done_callback(read_result)
    #         t.submit(func, "开", 5).add_done_callback(read_result)

    # get_dir_content()
    myclass = myClassTest("张")
    myclass.func()
    myClassTest.func()



zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
a, b = zip(*zipped)



