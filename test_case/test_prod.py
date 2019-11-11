from tools.api import request_tool
from tools.security.md5_tool import md5_passwd

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
def test_addProd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = "新增产品接口"  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "brand": "小米",
  "colors": [
    "鎏金黑","亮雪白"
  ],
  "price": 2468,
  "productCode": "自动生成 字符串 5 数字字母",
  "productName": "华为",
  "sizes": [
    "6"
  ],
  "type": "手机"
}   '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    pub_data["skuCode"]=r.json()["data"][0]["skuCode"]
# json path，参数类型为列表 根据jsonpath提取响应正文中的数据
#json_path = [{"skuCode": '$.data[0].skuCode'}]
#request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)



def test_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "修改商品价格_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None

    data = {"SKU":pub_data["skuCode"],"price":6000}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)



def test_product_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品库存模块"  # allure报告中一级分类
    story = '增量调整商品库存'  # allure报告中二级分类
    title = "增量调整_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":pub_data["skuCode"], "qty": 6000}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_order_sign_addOrder(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    headers = {"token": pub_data["token"]}
    #s="receiver=wxs1234&ordeerPrice=6000&receiverPhone=13245826994&key=guoya"
    #sign = md5_passwd(s,"")
    #pub_data["sign"]=sign
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
 {
  "ordeerPrice": 1000000000,
  "orderLineList": [
    {
      "qty": 2,
      "skuCode": "${pub_data}"
    }
  ],
  "receiver": "wxs1234",
  "receiverPhone": "13245825656",
  "receivingAddress": "string",
  "sign": "string",
  "userName": "string"
}   '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_order_sign_addOrder(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    headers = {"token": pub_data["token"]}
    s="receiver=wxs1234&ordeerPrice=6000&receiverPhone=13245825656&key=guoya"
    sign = md5_passwd(s,"")
    pub_data["sign"]=sign
    #post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
 {
  "ordeerPrice": 1000000000,
  "orderLineList": [
    {
      "qty": 2,
      "skuCode": "${pub_data}"
    }
  ],
  "receiver": "string",
  "receiverPhone": "13245825656",
  "receivingAddress": "string",
  "sign": "${sign}",
  "userName": "string"
}   '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)



