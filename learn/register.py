# # coding=utf-8
# import json
# import random
# import time
# import urllib2
#
# def request():
#     try:
#         url = "http://www.xcj.com/index.php/index/User/register.html"
#         values = {'username': 'qwe123456', 'password': '123456'}
#         data = json.JSONEncoder().encode(values)
#         user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         headers = {'User-Agent' : user_agent, 'Content-type':"application/json"}
#         req = urllib2.Request(url, data=data, headers=headers)
#         res_data = urllib2.urlopen(req)
#         res = res_data.read()
#
#         print "response:" + str(len(res))
#         print(values)
#         if res_data.getcode() == 200:
#             return res
#     except urllib2.HTTPError, err:
#         print(err.code)
#         print(err.read())
#         raise
#
# def sendEmail():
#     try:
#         url = "https://www.xcj.com/user/sendesms"
#         values = {'email': 'mt@xcj.com'}
#         data = json.JSONEncoder().encode(values)
#         user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#         headers = {'User-Agent' : user_agent, 'Content-type':"application/json"}
#         req = urllib2.Request(url, data=data, headers=headers)
#         res_data = urllib2.urlopen(req)
#         res = res_data.read()
#
#         print "response:" + str(len(res))
#         print(values)
#         if res_data.getcode() == 200:
#             return res
#     except urllib2.HTTPError, err:
#         print(err.code)
#         print(err.read())
#         raise
#
# if __name__ == "__main__":
#     # mes = request()
#     # print(mes)
#     #sendEmail()
#     for i in range(1,10000):
#         sendEmail()
#         print("第[%d]封邮件" % i)
#         # 休眠1秒
#         time.sleep(1)
