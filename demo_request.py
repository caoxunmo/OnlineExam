from lib.config import HOST
import requests
import pprint
import hashlib
"""
URL：http://121.41.14.39:9097/api/loginS
请求头：Content-Type: application/json
请求体：{ 
            "username": "20200011", 
            "password": "e10adc3949ba59abbe56e057f20f883e" 
}
"""

# 登录操作
url = f"{HOST}/api/loginS"
# print(url)
payload = {
    "username": "20200011 ",
    "password": "e10adc3949ba59abbe56e057f20f883e"
}

# 密码加密(md5方式)
def get_md5Data(param):
    md5 = hashlib.md5()     # 实例化md5
    md5.update(param.encode('utf-8'))   # 加密
    return md5.hexdigest()

#print(get_md5Data('123456'))

'''
data ----> 表单形式的参数
json ----> json格式的参数
'''

resp = requests.post(url, json=payload)
# print(resp.text)
# print(type(resp.text))       # 返回的是字符串类型
# print(resp.json())
# print(type(resp.json()))       # 返回的是字典---要求响应是JSON
pprint.pprint(resp.json())
res = resp.json()
print("token值：%s" % res['token'])
