import requests
from reptile.DBO import dbo
from bs4 import BeautifulSoup
import time

# 数据库操作类
dbo = dbo()

# count 条目数
count = 0



# 模拟ajax请求,拉取人物信息
'''
    num:请求多少次(默认每次10条)  
'''
def figure(num):
    global count
    try:

        for i in range(0, num):
            url = "http://nanrenvip.net/e/action/get_more_nvyou.php"
            data = {"next": i, "table": "nvyou", "action": "getmorenvyou", "limit": 10, "small_length": 10,
                    "orderby": "onclick"}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

            respone = requests.post("http://nanrenvip.net/e/action/get_more_nvyou.php", data=data)
            if respone.text.__len__() > 1:
                soup = BeautifulSoup(respone.text, 'lxml')
                ips = soup.find_all('li')

                for i in range(1, len(ips)):
                    ip_info = ips[i]
                    tds = ip_info.find_all('a')
                    # print("别名:%s" % tds[0].attrs['href'])
                    # print("名字:%s" % tds[0].text)
                    # print("图片:%s" % tds[0].next_element.attrs['src'])

                    dbo.insertFigure(tds[0].text, tds[0].next_element.attrs['src'], tds[0].attrs['href'])

                    count = count + 1
            else:
                break
            time.sleep(2)
    except Exception as e:
        print("拉取到:%s条" % count)
        print(e)


#根据数据库中查询到人物信息，爬取相关fanhao
def figure_source():
    #所有人物Id
    figureData = dbo.getAllFigure()

    for i in figureData:
        print(i)
    pass


if __name__ == "__main__":
    # print("开始爬取..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # figure(10000)
    # print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # print("拉取到:%s条" % count)

    figure_source()
