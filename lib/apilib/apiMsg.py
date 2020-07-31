from lib.config import HOST, userData, msgData
from apiLogin import LoginClass
import requests
from pprint import pprint


class MsgClass:
    # 新增留言接口
    def add_msg(self, inToken, inData):
        url = f'{HOST}/api/message'
        header = {'Content-Type': 'application/json', 'X-AUTH-TOKEN': inToken}
        payload = inData
        resp = requests.post(url, json=payload, headers=header)
        return resp.json()


if __name__ == '__main__':
    # 获取登录的Token值
    resp = LoginClass().login('POST', userData)
    token = resp['token']
    print(f'登录返回的Token值：{token}')

    # 验证留言接口
    msg = MsgClass()
    res = msg.add_msg(inToken=token, inData=msgData)
    pprint(res)
























'''
# 留言模块
# URL
url = f'{HOST}/api/message'

# Token值
testData = {
        "username": "20200011 ",
        "password": "123456"
}
token = lg.login('POST', testData)['token']
print(f'token值是：{token}')
'''