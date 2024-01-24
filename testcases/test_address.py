#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: allen lv
@file: test_order.py
@time: 2024/1/19 2:06
desc: 测试用例 address
"""

import pytest
from db.db import DB
import json
from utils.request import Request

# db = DB()


# 使用 fixture 实现全局变量
@pytest.fixture(scope="session")
def global_data():
    return {"aid": None}


# 获取地址列表 数据源
def data_getaddresslist():
    SQL = "SELECT * from address " \
          "WHERE id = '001'  AND name='succ-getAddressList' "
    data = db.executeSql(SQL)
    return data


# 获取地址列表 用例
@pytest.mark.parametrize("result", data_getaddresslist())
def test_getsAddressList(result, getToken):
    cookie = getToken
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    data = result[7]
    expect_result = result[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    res = Request.send_request(url, method=request_type, data=dataDict, cookies=cookie).json()
    assert expect_resultDict["errno"] == res["errno"]
    assert expect_resultDict["message"] == res["message"]


# 添加新地址 数据源
def data_addNewAddress():
    SQL = "SELECT * from address " \
          "WHERE (id = '002' OR id = '003') " \
          "AND ( name='succ-addNewAddress' OR  name='fail-addNewAddress') "
    data = db.executeSql(SQL)
    return data


# 添加新地址 用例
@pytest.mark.parametrize("result", data_addNewAddress())
def test_addNewAddress(result, getToken, global_data):
    cookie = getToken
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    data = result[7]
    expect_result = result[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    res = Request.send_request(url, method=request_type, data=dataDict, cookies=cookie).json()
    if res["errno"] == 0:
        global_data["aid"] = res["data"]["_id"]
        # pytest.AddressId =
    assert expect_resultDict["errno"] == res["errno"]
    assert expect_resultDict["message"] == res["message"]


# 根据 aid 获取地址 数据源
def data_getAddressByAid():
    SQL = "SELECT * from address " \
          "WHERE (id = '004' OR id = '005') " \
          "AND ( name='succ-getAddressByAid' OR  name='fail-getAddressByAid-wrongid') "
    data = db.executeSql(SQL)
    return data


# 根据 aid 获取地址 用例
@pytest.mark.parametrize("result", data_getAddressByAid())
def test_getAddressByAid(result, getToken, global_data):
    cookie = getToken
    id = result[0]
    name = result[1]
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    expect_result = result[8]
    url = 'http://' + request_prefix + request_url
    expect_resultDict = json.loads(expect_result)
    aid = 123
    if id == '004' and name == 'succ-getAddressByAid':
        aid = global_data["aid"]
    url = url + str(aid)
    res = Request.send_request(url, method=request_type, cookies=cookie).json()
    assert expect_resultDict["errno"] == res["errno"]
    assert expect_resultDict["message"] == res["message"]


# 根据 aid 更新地址 数据源
def data_updateAddressByAid():
    SQL = "SELECT * from address " \
          "WHERE (id = '006' OR id = '007') " \
          "AND ( name='succ-updateAddress' OR  name='fail-updateAddress') "
    data = db.executeSql(SQL)
    return data


# 根据 aid 更新地址 用例
@pytest.mark.parametrize("result", data_updateAddressByAid())
def test_updateAddressByAid(result, getToken, global_data):
    cookie = getToken
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    data = result[7]
    expect_result = result[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    aid = global_data["aid"]
    url = url + str(aid)
    res = Request.send_request(url, method=request_type, cookies=cookie, data=dataDict).json()
    assert expect_resultDict["errno"] == res["errno"]
    assert expect_resultDict["message"] == res["message"]


# 根据 aid 删除地址 数据源
def data_delAddressByAid():
    SQL = "SELECT * from address " \
          "WHERE (id = '008' OR id = '009') " \
          "AND ( name='succ-delAddress' OR  name='fail-delAddress') "
    data = db.executeSql(SQL)
    return data


# 根据 aid 删除地址 用例
@pytest.mark.parametrize("result", data_delAddressByAid())
def test_delAddressByAid(result, getToken, global_data):
    cookie = getToken
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    data = result[7]
    expect_result = result[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    aid = global_data["aid"]
    url = url + str(aid)
    res = Request.send_request(url, method=request_type, cookies=cookie, data=dataDict).json()
    assert expect_resultDict["errno"] == res["errno"]
    assert expect_resultDict["message"] == res["message"]


# 获取用户默认地址 数据源
def data_getDeafultAddress():
    SQL = "SELECT * from address " \
          "WHERE id = '010' AND name='succ-getDefaultAddress'  "
    data = db.executeSql(SQL)
    return data


# 获取用户默认地址 用例
@pytest.mark.parametrize("result", data_getDeafultAddress())
def test_getDeafultAddress(result, getToken, global_data):
    cookie = getToken
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    data = result[7]
    expect_result = result[8]
    url = 'http://' + request_prefix + request_url
    dataDict = json.loads(data)
    expect_resultDict = json.loads(expect_result)
    res = Request.send_request(url, method=request_type, cookies=cookie, data=dataDict).json()
    assert expect_resultDict["errno"] == res["errno"]
    assert expect_resultDict["message"] == res["message"]


if __name__ == '__main__':
    pytest.main(['test_address.py', '-v'])
