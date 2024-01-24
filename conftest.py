#!/usr/bin/env python
# encoding: utf-8
# @author: allen lv
# @file: test.py
# @time: 2024/1/16 20:58
# @desc: 全局 测试固件
import pytest
from db.db import DB
from utils.request import Request
import json
from itertools import chain

#

@pytest.fixture(scope='session')
def getToken():
    print('module start')
    db = DB()
    SQL = "SELECT * from user " \
          "WHERE id = '001' AND name='succ-login' "
    data = db.executeSql(SQL)
    result = list(chain.from_iterable(data))
    # print('result==>', result, type(result))
    request_prefix = result[3]
    request_url = result[4]
    request_type = result[5]
    data = result[7]
    dataDict = json.loads(data)
    url = 'http://' + request_prefix + request_url
    res = Request.send_request(url, method=request_type, data=dataDict)
    cookies = res.cookies
    db.close()
    yield cookies
    print('module end')




if __name__ == '__main__':
    pytest.main(['conftest.py', '-v'])