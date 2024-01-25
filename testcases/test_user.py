#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: allen lv
@file: test_order.py
@time: 2024/1/19 2:06
desc: 测试用例 user
"""

import pytest
from db.db import db
import json
from utils.request import Request


# 数据库对象
# db = DB()


# 获取 login 数据源
def data_login():
    SQL = "SELECT * from user " \
          "WHERE (id = '001' OR id = '002' OR id = '003') " \
          "AND (name='succ-login' OR name='error-username_fail' OR name='error-password_fail')"
    data = db.executeSql(SQL)
    return data


@pytest.mark.parametrize("res", data_login())
def test_login(res):

    request_prefix = res[3]
    request_url = res[4]
    request_type = res[5]
    data = res[7]
    expect_result = res[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    resp = Request.send_request(url, method=request_type, data=dataDict).json()
    assert expect_resultDict["errno"] == resp["errno"]
    assert expect_resultDict["message"] == resp["message"]


# 获取 register 数据源
def data_register():
    SQL = "SELECT * from user " \
          "WHERE (id = '004' OR id = '005' OR id = '006') " \
          "AND (name='succ-register' OR name='error-username_repeat_fail' OR " \
          "name='error-username_confirmpassword_fail')"
    data = db.executeSql(SQL)
    return data


@pytest.mark.parametrize("res", data_register())
def test_register(res):
    request_prefix = res[3]
    request_url = res[4]
    request_type = res[5]
    data = res[7]
    expect_result = res[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    resp = Request.send_request(url, method=request_type, data=dataDict).json()
    assert expect_resultDict["errno"] == resp["errno"]
    assert expect_resultDict["message"] == resp["message"]


if __name__ == '__main__':
    pytest.main(['test_user.py', '-v'])
