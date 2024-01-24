#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: allen lv
@file: test_order.py
@time: 2024/1/19 2:06
desc: 测试用例 user
"""

import pytest
from db.db import DB
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


@pytest.mark.parametrize("result", data_login())
def test_login(result):
    id = result[0]
    name = result[1]
    module = result[2]
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    need_login = result[6]
    data = result[7]
    expect_result = result[8]
    real_result = result[9]
    test_result = result[10]
    data_type = result[11]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    # print( dataDict, type(dataDict),expect_resultDict, type(expect_resultDict))
    res = Request.send_request(url, method=request_type, data=dataDict).json()
    # print('res==>',res)
    assert  expect_resultDict["errno"]==res["errno"]
    assert  expect_resultDict["message"] ==  res["message"]



# 获取 register 数据源
def data_register():
    SQL = "SELECT * from user " \
          "WHERE (id = '004' OR id = '005' OR id = '006') " \
          "AND (name='succ-register' OR name='error-username_repeat_fail' OR name='error-username_confirmpassword_fail')"
    data = db.executeSql(SQL)
    return data


@pytest.mark.parametrize("result", data_register())
def test_register(result):
    id = result[0]
    name = result[1]
    module = result[2]
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    need_login = result[6]
    data = result[7]
    expect_result = result[8]
    real_result = result[9]
    test_result = result[10]
    data_type = result[11]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    # print( url, dataDict, type(dataDict),expect_resultDict, type(expect_resultDict))
    res = Request.send_request(url, method=request_type, data=dataDict).json()
    # print('res==>',res)
    assert  expect_resultDict["errno"]==res["errno"]
    assert  expect_resultDict["message"] ==  res["message"]