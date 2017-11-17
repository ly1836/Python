import requests
from reptile.DBO import dbo
from bs4 import BeautifulSoup
import time
import sys
import emailTest

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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    url = "http://nanrenvip.net/e/action/get_more_nvyou.php"
    try:

        for i in range(0, num):

            data = {"next": i, "table": "nvyou", "action": "getmorenvyou", "limit": 10, "small_length": 10,
                    "orderby": "onclick"}
            respone = requests.post(url, data=data)
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
        print("拉取到:%d条" % count)
        print(e)


# 根据数据库中查询到人物信息，爬取相关fanhao
def figure_source():
    global count

    # 所有人物
    figureData = dbo.getAllFigure()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    url = "http://nanrenvip.net/e/action/get_more_index.php"

    try:
        for i in figureData:
            # 人物ID
            figureId = i[0]

            # 要获得fanhao的地址
            url = "http://nanrenvip.net/%s" % i[3]
            urls = url

            for j in range(1, 100):
                if j > 1:
                    url = "%sindex_%d.html" % (urls, j)

                respone = requests.get(url, headers=headers)
                if respone.text.find("404 Not Found") == -1:
                    soup = BeautifulSoup(respone.text, 'lxml')
                    li = soup.find_all('li', {"class": "post"})

                    for k in range(0, li.__len__()):
                        # 图片地址
                        img_src = li[k].find("img").attrs['data-original']

                        # fanhao
                        source = li[k].find("b").text

                        # 时间
                        date = li[k].findAll("date")[1].text

                        dbo.insertFigureSource(source, img_src, date, figureId)

                        count = count + 1
                else:
                    break

            time.sleep(2)

    except Exception as e:
        print("拉取到:%d条" % count)
        print(e)


# ajax请求获得fanhao页面的data数据
def getAjaxData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    respone = requests.get(url, headers=headers)
    soup = BeautifulSoup(respone.text, 'lxml')

    js = soup.find_all('script')
    ajax = str(js[js.__len__() - 2].text)

    strs = ajax[ajax.find('data'):ajax.find('}') + 1]

    return strs


'''
    根据数据库中fanhao,查找[http://www.btsoso.info/search/[]_ctime_1.html] 中magnet详细信息
'''


def magnet_source(id):
    global count

    # 所有fanhao
    sourceData = dbo.getAllSource(id)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    url = "http://www.btrabbit.cc/search/"

    source_id = 0
    try:
        for source in sourceData:
            # fanhao ID
            source_id = source[0]

            url = "http://www.btsoso.info/search/%s_ctime_1.html" % source[1]

            respone = requests.get(url, headers=headers)
            soup = BeautifulSoup(respone.text, 'lxml')

            div = soup.find_all('a', {"class": "title"})

            if div.__len__() > 0:
                for a in div:
                    # print(a.attrs['href'])
                    getMagnetInfoByUrl("http://www.btsoso.info/%s" % a.attrs['href'], source_id)

            #调用进度条
            view_bar(source_id,sourceData.__len__())

            #休眠0.5秒,防止网站安全机制
            time.sleep(0.5)

    except Exception as e:
        print("拉取到:%d条" % count)
        print(e)
        print("进行重连...")
        rate = source_id / sourceData.__len__()
        rate_num = float(rate * 100)
        emailTest.send_mail("491816301@qq.com", "爬虫错误日志", "%s\n进度:%.5f%%\n进行重连..." % (str(e),rate_num))
        magnet_source(source_id)


'''
    根据URL获取magnet详细信息,并且保存到数据库中
'''


def getMagnetInfoByUrl(url, sourceId):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        respone = requests.get(url, headers=headers)
        soup = BeautifulSoup(respone.text, 'lxml')

        textarea = soup.find('textarea', {"id": "magnetLink"})

        tr = soup.find_all("tr")
        if (textarea.text is None) or (tr[1].find_all("td")[1].text is None) or (tr[2].find_all("td")[1].text is None):
            return
        magnetLink = textarea.text
        fileSize = tr[1].find_all("td")[1].text
        date = tr[2].find_all("td")[1].text

        dbo.insertMagent(date, fileSize, magnetLink, sourceId)
    except Exception as e:
        print("连接断开,ID:%d" % sourceId)
        print(e)
        print("进行重连...")
        emailTest.send_mail("491816301@qq.com", "爬虫错误日志", "%s,进行重连..." % str(e))
        magnet_source(sourceId)

# 进度条实现方法
def view_bar(num,total):
    rate = num / total
    rate_num = float(rate * 100)
    #r = '\r %d%%' %(rate_num)
    r = '\r%s>%.5f%%' % ('=' * int(rate_num), rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush

if __name__ == "__main__":
    # print("开始爬取..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # figure(10000)
    # print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # print("拉取到:%d条" % count)

    # print("开始爬取..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # figure_source()
    # print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    print("开始爬取..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    magnet_source(18365)
    print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    emailTest.send_mail("491816301@qq.com", "通知", "爬取结束!")


