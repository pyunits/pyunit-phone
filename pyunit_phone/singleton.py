# !/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/6/28 下午4:33
# @Author: Jtyoui@qq.com
# @Notes : 通过单例模式的方法创建的类在当前进程中只有一个实例
import threading
from functools import wraps


def singletons(cls):
    """单例模式"""
    instance = {}
    _lock = threading.Lock()  # 实现线程锁，增加安全性

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            with _lock:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper
