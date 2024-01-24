#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: allen lv
@file: test_order.py
@time: 2024/1/19 2:06
desc: 测试用例 order
"""
import pytest
from db.db import DB
import json
from utils.request import Request

# 数据库对象
# db = DB()


# 获取订单提交 数据源
def data_order_submit():
    SQL = "SELECT * from orders " \
          "WHERE (id = '001' OR id = '002' ) AND (name='succ_order_commit' OR name='fail_order_commit') "
    data = db.executeSql(SQL)
    return data

# 获取订单提交 测试用例
@pytest.mark.parametrize("result", data_order_submit())
def test_order_submit(result,getToken):
    cookie= getToken
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
    res = Request.send_request(url, method=request_type, json=dataDict, cookies=cookie).json()
    assert  expect_resultDict["errno"]==res["errno"]
    assert  expect_resultDict["message"] ==  res["message"]


# 获取全部订单 数据源
def data_order_getall():
    SQL = "SELECT * from orders " \
          "WHERE id = '003'  AND name='succ_order_getAll' "
    data = db.executeSql(SQL)
    return data

# 获取订单提交 测试用例
@pytest.mark.parametrize("result", data_order_getall())
def test_order_getall(result,getToken):
    cookie= getToken
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
    res = Request.send_request(url, method=request_type, json=dataDict, cookies=cookie).json()
    assert  expect_resultDict["errno"]==res["errno"]
    assert  expect_resultDict["message"] ==  res["message"]