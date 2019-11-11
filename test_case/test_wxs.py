# -*- coding: utf-8 -*-
# @Project: guoya-app-test
# @Author: 小吴老师
# @Email: wuling@guoyasoft.com
# @Weichat: 875955899
# @Create time: 2019/9/22 8:28

# 请在terminal窗口输入下方命令：
# pip3 install gy-api-tools
# -*- coding:utf-8 -*-
# 右键-run 运行下列代码
from tool.init_project import *

from tools.api import request_tool

def test_signup(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''{
  "phone": "13245829651",
  "pwd": "wxs1234",
  "rePwd": "wxs1234",
  "userName": "wxs12345"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果

def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "login"  # 接口地址

    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''{
  "pwd": "wxs1234",
  "userName": "wxs12345"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)

    data = {'token' :r.json() ["data"]["token"]}
    return data





