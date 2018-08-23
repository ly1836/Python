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
    def getEncryptedCurrency(self, shortName):
        sql = "SELECT * from b_encrypted_currency where shortName_ = \"" + shortName + "\""
        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            return data
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()

    # 插入HitBTC交易对
    def insertExchangePair(self, createDate, lastUpdateDate, version, exchangeId, originalPair, baseCurrency,
                           quoteCurrency,
                           baseCurrencyId, exchangeName, exchangeUrl):
        sql = ""
        if (baseCurrencyId == -1):
            sql = "insert into b_exchange_pair(createDate_,lastUpdateDate_,version_,exchangeId_,originalPair_,baseCurrency_,quoteCurrency_,exchangeName_,exchangeUrl_) value(\"" + createDate + "\",\"" + lastUpdateDate + "\",%d,%d,%s,%s,%s,%s,%s)" % (
                version, exchangeId, "\"" + originalPair + "\"", "\"" + baseCurrency + "\"",
                "\"" + quoteCurrency + "\"",
                "\"" + exchangeName + "\"", "\"" + exchangeUrl + "\"")
        else:
            sql = "insert into b_exchange_pair(createDate_,lastUpdateDate_,version_,exchangeId_,originalPair_,baseCurrency_,quoteCurrency_,baseCurrencyId_,exchangeName_,exchangeUrl_) value(\"" + createDate + "\",\"" + lastUpdateDate + "\",%d,%d,%s,%s,%s,%d,%s,%s)" % (
                version, exchangeId, "\"" + originalPair + "\"", "\"" + baseCurrency + "\"",
                "\"" + quoteCurrency + "\"",
                baseCurrencyId, "\"" + exchangeName + "\"", "\"" + exchangeUrl + "\"")
        try:
            self.__cursor.execute(sql)

            # 提交到数据库执行
            self.__db.commit()
        except:
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()

    # 查询所有交易对信息
    def getExchangePair(self):
        sql = "select *from b_exchange_pair"

        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            return data
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()

    def HitBTC(self, url, exchangePair, exchangeName, exchangeId, exchangeUrl):
        counts = 0
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            s = requests.session()
            s.proxies = {'https': '127.0.0.1:1080'}
            respone = s.get(url, headers=headers)

            if respone.text.__len__() > 1:
                d = json.loads(respone.text)
                for i in range(0, len(d)):
                    # 基础币种
                    baseCurrency = d[i]['baseCurrency']
                    # 计价币种
                    quoteCurrency = d[i]['quoteCurrency']
                    # 完整交易对
                    symbol = baseCurrency + quoteCurrency

                    #过滤DAI币种
                    if(baseCurrency == "DAI" or quoteCurrency == "DAI"):
                        print("过滤[%s]交易对" % symbol)
                        continue

                    flag = 1
                    for j in range(0, len(exchangePair)):
                        #print(symbol)
                        #if(symbol == "btcusdt"):
                            #print(exchangePair[j][5])
                        if (exchangePair[j][5] == symbol and exchangePair[j][4] == exchangeId):
                            flag = 0
                    if (flag == 1):

                        counts = counts + 1
                        nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # baseCurrency = (d[i]['symbol'] + "")[0:((d[i]['symbol'] + "").index("_"))]
                        # quoteCurrency = (d[i]['symbol'] + "")[
                        #                 (d[i]['symbol'] + "").index("_") + 1:len(d[i]['symbol'] + "")]
                        data = db.getEncryptedCurrency(baseCurrency)

                        if (data.__len__() == 0):
                            db.insertExchangePair(nowDate, nowDate, 1, exchangeId, symbol, baseCurrency,
                                                  quoteCurrency, -1, exchangeName, exchangeUrl)
                        else:
                            baseCurrencyId = data[0][0]

                            db.insertExchangePair(nowDate, nowDate, 1, exchangeId, symbol, baseCurrency,
                                                  quoteCurrency, baseCurrencyId, exchangeName, exchangeUrl)

                        print("数据库中未找到[%s]交易对,已入库" % symbol)
            print("已入库[%d]个交易对" % counts)
        except Exception as e:
            print("拉取HitBTC交易对失败")
            print(e)



    def reptilePage(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        s = requests.session()
        s.proxies = {'https': '127.0.0.1:1080'}
        respone = s.get(url, headers=headers)

        soup = BeautifulSoup(respone.text, 'html')

        print(soup)



if __name__ == "__main__":
    db = dbo()

    #db.reptilePage("https://hitbtc.com/")

    exchangePair = db.getExchangePair()
    db.HitBTC("https://api.hitbtc.com/api/2/public/symbol", exchangePair,"Hitbtc",14,"https://hitbtc.com")
    print("HitBTC交易对同步完毕")
