import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import emailTest
import win32file
from reptile.DBO import dbo
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

# 数据库操作类
dbo = dbo()

# count 条目数
count = 2


def start(num):
    global count
    try:

        for j in range(num, 209):
            webUrl = "http://www.7m02.com/recent/%s/" % j

            respone = requests.get(webUrl, headers=headers)

            if respone.text.__len__() > 1:
                soup = BeautifulSoup(respone.text, 'lxml')
                li = soup.find_all('li', {"id": re.compile('video-*')})

                for i in range(0, len(li)):
                    title = li[i].find("a").attrs['title']
                    href = "http://www.7m02.com/%s" % li[i].find("a").attrs['href']
                    img = li[i].find("img").attrs['src']
                    playingTime = li[i].find("span", {"class", "video-overlay"}).text

                    fileName = "%d.mp4" % getDate()

                    respone = requests.get(href, headers=headers)

                    soup = BeautifulSoup(respone.text, 'lxml')

                    mp4Url = soup.find('source').attrs['src']

                    # 下载视频
                    #download(mp4Url, fileName)

                    # 对视频信息保存到数据库
                    dbo.insertVideo(title, img, playingTime, fileName, mp4Url)

                # 用于重连
                count = num + 1

            else:
                break

    except Exception as e:
        print(e)
        print("进行重连...")
        #emailTest.send_mail("491816301@qq.com", "爬虫错误日志", "%s\n进行重连..." % (str(e)))
        #start(count)


'''
    <p>获取当前时间戳，用来组成视频名</p>
'''


def getDate():
    t = time.time()

    return int(round(t * 1000))


'''
    <p>下载视频</p>
    @videoUrl 视频web url
    @fileName 随机生成的文件名
'''


def download(videoUrl, fileName):
    try:

        sectorsPerCluster, bytesPerSector, numFreeClusters, totalNumClusters \
            = win32file.GetDiskFreeSpace("h:\\")
        HDisSize = (numFreeClusters * sectorsPerCluster * bytesPerSector) / (1024 * 1024)

        sectorsPerCluster, bytesPerSector, numFreeClusters, totalNumClusters \
            = win32file.GetDiskFreeSpace("i:\\")
        IDisSize = (numFreeClusters * sectorsPerCluster * bytesPerSector) / (1024 * 1024)

        if HDisSize > 0:
            urllib.request.urlretrieve(videoUrl, 'H:\\video\\%s' % fileName)

        elif IDisSize > 0:

            urllib.request.urlretrieve(videoUrl, 'I:\\video\\%s' % fileName)
        else:
            emailTest.send_mail("491816301@qq.com", "爬虫错误日志", "磁盘空间已满，注意关停程序!!!")
    except Exception as ex:
        emailTest.send_mail("491816301@qq.com", "爬虫错误日志", "%s\n视频下载错误，请查明情况!!!" % str(ex))


if __name__ == "__main__":
    print("stand")

    data = dbo.getVideo(1045)
    for i in data:
        download(i[5],i[4])

    #start(85)

    print('end')
