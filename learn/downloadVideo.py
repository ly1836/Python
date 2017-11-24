import urllib.request

print("stand")

videoUrl = "http://www.7m02.com/file/6138/2/e87e7617f1201aae5c29/1511352458/mobile/6138.mp4"

urllib.request.urlretrieve(videoUrl,'G:\\downloadVideo\\6138.mp4')


print('end')