# -*- coding:utf-8 -*-
# 扇贝单词爬虫
# author: weijia
# MongoDB 参考  https://www.cnblogs.com/melonjiang/p/6536876.html
# 多线程 参考  http://www.jianshu.com/p/544d406e0875

import requests
import json
import threading
import time
import Queue
from pymongo import MongoClient

SHARE_Q = Queue.Queue()  # 构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 5  # 设置线程的个数

conn = MongoClient('localhost', 27017)
db = conn.words  # 连接mydb数据库，没有则自动创建
cl_words = db.cl_words  # 使用test_set集合，没有则自动创建


class MyThread(threading.Thread):
    """
        func: 线程函数逻辑
    """

    def __init__(self, func):
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.func = func  # 传入线程函数逻辑

    def run(self):
        """
        重写基类的run方法

        """
        self.func()


def save_vocabulary_info(json_info):
    cl_words.insert(json_info)


def download_vocabulary(vocabulary_id):
    url = 'https://www.shanbay.com/api/v1/bdc/example/?type=sys&vocabulary_id=' + str(vocabulary_id)
    print url
    try:
        res = requests.get(url)
        json_result = json.loads(res.content, encoding='UTF-8')
        if json_result['status_code'] == 0 and len(json_result['data']) != 0:
            word = json_result['data'][0]['word']
            # 查询数据
            url = 'https://api.shanbay.com/bdc/search/?word=' + word
            res = requests.get(url)
            json_result = json.loads(res.content, encoding='UTF-8')
            if json_result['status_code'] == 0:
                save_vocabulary_info(json_result)
                print '成功下载单词:' + word
                return
            print '下载失败:' + word
    except BaseException, arguement:
        print arguement
        if str(arguement).find('JSON') != -1:
            print 'IP被禁,无法爬虫.'
            exit(1)


def worker():
    """
    主要用来写工作逻辑, 只要队列不空持续处理
    队列为空时, 检查队列, 由于Queue中已经包含了wait,
    notify和锁, 所以不需要在取任务或者放任务的时候加锁解锁
    """
    global SHARE_Q
    while True:
        if not SHARE_Q.empty():
            item = SHARE_Q.get()  # 获得任务
            download_vocabulary(item)
            time.sleep(1)
            SHARE_Q.task_done()


def main():
    start_time = time.localtime()
    global SHARE_Q
    threads = []
    # 向队列中放入任务, 真正使用时, 应该设置为可持续的放入任务
    for task in xrange(1, 100000):  # TODO 从1 爬到 100000
        SHARE_Q.put(task)
    # 开启_WORKER_THREAD_NUM个线程
    for i in xrange(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()  # 线程开始处理任务
        threads.append(thread)
    for thread in threads:
        thread.join()
    # 等待所有任务完成
    SHARE_Q.join()
    end_time = time.localtime()
    print "开始时间:", time.strftime("%Y-%m-%d %H:%M:%S", start_time)
    print "结束时间:", time.strftime("%Y-%m-%d %H:%M:%S", end_time)


if __name__ == "__main__":
    main()
