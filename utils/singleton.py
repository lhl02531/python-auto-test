#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: allen lv
@file: singleton.py
@time: 2024/1/25 16:56
desc: 单例装饰器
"""
def singleton(cls):
    instance = {}

    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _singleton
