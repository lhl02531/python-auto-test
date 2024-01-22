#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: allen lv
@file: request.py
@time: 2024/1/17 22:41
desc: 请求通用类
"""
import requests


class Request:

    @staticmethod
    def send_request(url, method='get', params=None, data=None, json=None, cookies=None, timeout=1000):
        result = None
        if method == 'get':
            result = requests.get(url, params=params, data=data, json=json,cookies=cookies, timeout=timeout)
        elif method == 'post':
            result = requests.post(url, data=data, cookies=cookies, timeout=timeout)
        elif method == 'delete':
            result = requests.delete(url, data=data, cookies=cookies, timeout=timeout)
        elif method == 'patch':
            result = requests.patch(url, data=data, cookies=cookies, timeout=timeout)
        else:
            raise Exception('请求方式不支持: {}'.format(method))
        return result


# url = 'http://localhost:3000/api/shop/hot-list'
# method = 'post'
#
# result = Request.send_request(url)
# print('result', result, result.json())

# url1 = 'http://localhost:3000/api/user/login'
# method1 = 'post'
# result1 = Request.send_request(url1, method=method1, data={"username": "test3", "password": "test3"})
# print('result', result1, result1.json(), result1.cookies)
