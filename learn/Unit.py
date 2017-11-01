# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用
from urllib import request

from bs4 import BeautifulSoup
import requests
import pymysql
import time
import logging

class unit:
    # 初始化数据库操作
    def __init__(self):
        # 打开一个数据库连接
        self.__db = pymysql.connect("localhost", "root", "admin", "pydb", charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.__cursor = self.__db.cursor()

        print("数据库连接已建立")

    def DB(self,proxies):
        sql = "insert into user(name,sex,age) VALUE('王五',12,'123')"

        try:
            i = 0
            # 执行sql语句
            while True:
                if i > 100000:
                    break
                self.__cursor.execute(sql)
                i += 1

            # 提交到数据库执行
            self.__db.commit()
            print("数据插入成功")
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
        finally:
            self.__db.close()

            print("关闭数据库连接")



def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        if tds[5].text == "HTTPS":
            ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    # proxy_ip = random.choice(proxy_list)
    # proxies = {'https': proxy_ip}
    return proxy_list

#保存到本地文件
def save(saveFilePath):

    i=1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    url = ''
    proxies = []
    while True:
        if (i <= 10):
            url = 'http://www.xicidaili.com/nn/%d' % i
            ip_list = get_ip_list(url, headers=headers)
            proxies.append(get_random_ip(ip_list))
            i += 1
            pass
        else:
            break

    print(proxies)
    f = open(saveFilePath, "w")
    for i in proxies:
        f.write(str(i))
    f.close()
    print("size %d" % len(proxies))

#保存到数据库
def saveDB():
    print("开始爬取..:%s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    i = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    proxies = []
    while True:
        if (i <= 10):
            url = 'http://www.xicidaili.com/nn/%d' % i
            ip_list = get_ip_list(url, headers=headers)
            proxies.append(get_random_ip(ip_list))
            i += 1
            pass
        else:
            break

    print(proxies)
    print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    pass




#解析文件中url
def parseData(path):
    f = open(path, "r")
    str = f.read()

    s = str.strip('\[')
    s = s.strip('\]')
    s = s.strip()
    # 根据逗号切割成数组
    str = s.split(",")

    strLists = []
    strList = []
    for i in str:
        strLists.append(i.strip("'").strip(" '").strip("']['").split("']['"))

    for i in strLists:
        for j in i:
            strList.append(j)

    return  strList

def test():
    # 访问网址
    url = 'http://ly1836.github.io'
    # 这是代理IP
    proxy = {'https': '218.56.132.154:8080'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')]
    # 安装OPener
    request.install_opener(opener)
    # 使用自己安装好的Opener
    response = request.urlopen(url)
    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    # 打印信息
    print(html)

if __name__ == '__main__':
    db = unit()


    saveDB()

    #save("d:/Reptile.txt")
    # parseData("d:/Reptile.txt")
    #
    # list = parseData("d:/Reptile.txt")
    #
    # BlogUrl = "http://www.leiyang.group"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    #
    # for i in list:
    #     web_data = requests.get(BlogUrl, proxies={'http':i})
    #     print(web_data.text)
    # test()





