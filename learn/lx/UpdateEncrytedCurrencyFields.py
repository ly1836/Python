import json
import requests
import pymysql
import logging
import datetime
from bs4 import BeautifulSoup



class dbo:
    # 初始化数据库操作
    def __init__(self):
        # 打开一个数据库连接
        self.__db = pymysql.connect("localhost", "root", "admin123", "lianxiang", charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.__cursor = self.__db.cursor()

        print("数据库连接已建立")

    # 根据基础币种Name查询baseCurrencyId
    def getEncryptedCurrency(self):
        sql = "SELECT * from b_encrypted_currency"
        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            return data
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()



    def feixiaohao(self,encryptedCurrency):
        noneSet = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        i = 0
        try:
            for j in range(1, len(encryptedCurrency)):
                url = "https://www.feixiaohao.com/search?word="
                respone = None
                soup = None
                href = ""
                context = ""
                if((encryptedCurrency[j][12] == None) or (encryptedCurrency[j][12]+"" == "") or (encryptedCurrency[j][12]+"" == "[]")):
                    url = url + encryptedCurrency[j][4]
                    respone = requests.get(url, headers=headers)
                    soup = BeautifulSoup(respone.text, 'html')
                    if(soup.find_all("a")[21].text == "EOS"):
                        url = "https://www.feixiaohao.com/search?word="
                        respone = None

                        url = url + encryptedCurrency[j][5]
                        respone = requests.get(url, headers=headers)
                        soup = BeautifulSoup(respone.text, 'html')


                    href = soup.find_all("a")[21].attrs['href']
                    href = str(href).replace("currencies","coindetails")
                    respone = requests.get("https://www.feixiaohao.com" + href, headers=headers)

                    soup = BeautifulSoup(respone.text, 'html')
                    if(soup.find_all("p").__len__() >= 2):
                        context = soup.find_all("p")[1].text
                        print("======%s========" % encryptedCurrency[j][5])
                        print(context)
                        i = i + 1
                    else :
                        noneSet.append(encryptedCurrency[j][5])
            print("从非小号查出[%d]个币种简介" % i)
            return noneSet
        except Exception as e:
            print("同步币种简介失败!")
            print(e)

if __name__ == "__main__":
    db = dbo()
    encryptedCurrency = db.getEncryptedCurrency()
    #db.updateEncytedCurrency("https://block.cc/api/v1/query?str=",encryptedCurrency)
    noneSet = db.feixiaohao(encryptedCurrency)
    print("======非小号简介为空:size[%d]=======" % noneSet.__len__())
    print(noneSet)
