#测试文件写入
def fileWrite():
    f = open("d:PythonFileWrite.txt", "w")

    f.write("测试文件写入")

    f.close()
    return


#测试文件读取
def fileRead():

    f = open("d:/PythonFileWrite.txt","r")

    str = f.read()

    print(str)
    return

#fileRead()


#爬取网页

from urllib import request

def reptile():
    respone = request.urlopen("http://www.baidu.com/")

    fi = open("d:/baidu.html","w")

    fi.write(str(respone.read()))

    fi.close()
    print("已爬取百度首页,保存文件路径:",str(fi.name))

    return

#reptile()


import pickle
def saveObj():
    # 使用pickle模块将数据对象保存到文件
    data1 = {'a': [1, 2.0, 3, 4 + 6j],
             'b': ('string', u'Unicode string'),
             'c': None}

    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)

    output = open('d:/data.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)

    # Pickle the list using the highest protocol available.
    pickle.dump(selfref_list, output, -1)

    output.close()
    return

#saveObj()


import pprint, pickle
def readObj():
    pkl_file = open('d:/data.pkl', 'rb')

    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    data2 = pickle.load(pkl_file)
    pprint.pprint(data2)

    pkl_file.close()
    return
#readObj()



#测试读写同时操作
def test():
    # 打开一个文件
    f = open(r"d:\foo.txt", "w+")

    f.write("sqweqwe\n")
    f.flush()

    str = f.readline()
    print(str)

    # 关闭打开的文件
    f.close()

#test()





