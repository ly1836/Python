import json
import requests
import pymysql
import logging
import datetime
from bs4 import BeautifulSoup


def login():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data ={"account":"ly1836","pwd":"18361836"}


    respone = requests.post("https://mobile.chainfor.com:8061/login/login", headers=headers,data=data,verify=False)
    d = json.loads(respone.text)


    return  d["appContentResponse"]

def logout(token):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'device_type': '2',
        'Authorization': token,
    }

    respone = requests.get("https://mobile.chainfor.com:8061/user/base/logout", headers=headers,verify=False)
    d = json.loads(respone.text)
    code = d['status']
    if (code == 1000):
        print("logout")

def userInfo(token):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'device_type': '2',
        'Authorization':token,

    }

    respone = requests.get("https://mobile.chainfor.com:8061/user/base/userInfo",headers=headers,verify=False)

    data = json.loads(respone.text)
    code = data['status']
    if(code == 1000):
        print("status:%d;msg:%s" % (code,data['msg']))
        return 1
    else:
        print("status:%d;msg:%s" % (code, data['msg']))
        return 2



def test():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',

    }

    proxies = {'http': '127.0.0.1:1080'}

    respone = requests.get("https://support.binance.com/hc/zh-cn", headers=headers,verify=False,proxies=proxies)
    soup = BeautifulSoup(respone.text, 'html')
    print(soup)



if __name__ == "__main__":

    # count = 1
    # for i in range(1, 1000):
    #     print("=======第[%d]次=============" % (count))
    #     token = login()
    #     if(userInfo(token) == 2):
    #         break
    #     else:
    #         logout(token)
    #         count = count + 1
    test()