from reptile.DBO import dbo
from bs4 import BeautifulSoup

import requests
import time

# 数据库操作类
dbo = dbo()

# count 条目数
count = 0


#
def get_ip_list(url, headers):
    global count
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')

        dbo.saveProxy(tds[1].text, tds[2].text, tds[5].text)

        count = count + 1

    return ip_list


# 开始爬取
def start(num):
    print("开始爬取..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    i = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    url = ''
    while True:
        if (i <= num):
            url = 'http://www.xicidaili.com/nn/%d' % i
            get_ip_list(url, headers=headers)
            i += 1

        else:
            break

    print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("共计:%d条" % count)


if __name__ == "__main__":
    start(2486)
