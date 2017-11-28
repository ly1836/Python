import time

from reptile.DBO import dbo
import requests

# 数据库操作类
dbo = dbo()

#根据数据库中图片网络地址，下载renwu图片
def figureImg():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    # 所有人物
    figureData = dbo.getAllFigure()

    for figure in figureData:
        url = str(figure[2])
        try:
            pic = requests.get(url, headers=headers, timeout=10)
            pass
        except requests.exceptions.ConnectionError:
            print('[错误]当前图片无法下载')
            continue
        fileName = r"G:\Reptile\figureImg\%s" % url[url.rfind("/") + 1:url.__len__()]

        fp = open(fileName, 'wb')
        fp.write(pic.content)
        fp.close()

#根据数据库中图片网络地址，下载fanhao图片
def sourceImg():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    # 所有fanhao
    sourceData = dbo.getAllSource(11093)

    for source in sourceData:
        url = str(source[2])
        try:
            pic = requests.get(url, headers=headers, timeout=10)
            pass
        except requests.exceptions.ConnectionError:
            print('[错误]当前图片无法下载')
            continue
        fileName = r"G:\Reptile\sourceImg\%s" % url[url.rfind("/") + 1:url.__len__()]

        fp = open(fileName, 'wb')
        fp.write(pic.content)
        fp.close()

        time.sleep(2)
    print("共下载:%d张" % sourceData.__len__())


if __name__ == "__main__":
    print("开始下载..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    sourceImg()
    print("爬取结束..:%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
