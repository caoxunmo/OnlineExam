from lib.config import HOST, userData
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

'''
data ----> 表单形式的参数
json ----> json格式的参数
'''


# 封装后的代码
'''
——————————登录模块————————
1、登录操作；2、md5加密；3、获取Token值
'''


class LoginClass():
    # def __init__(self, indata):
    #     self.indata = indata

    # 密码加密(md5方式)
    def get_md5Data(self, param):
        md5 = hashlib.md5()  # 实例化md5
        md5.update(param.encode('utf-8'))  # 加密
        return md5.hexdigest()

    def login(self, methods, indata):
        url = f"{HOST}/api/loginS"                                      # URL
        header = {'Content-Type': 'application/json'}                   # 请求头
        indata['password'] = self.get_md5Data(indata['password'])       # 加密后的值
        payload = indata
        resp = requests.request(method=methods, url=url, json=payload)
        return resp.json()

    # def get_token(self, methods, indata):
    #     token = self.login(methods, indata)['token']
    #     return token


if __name__ == '__main__':
    lg = LoginClass()
    res = lg.login('POST', userData)
    print(res, type(res))
# pprint.pprint(res)
# print(type(testData))

