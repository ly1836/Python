import json
import requests
import pymysql
import logging
import datetime



class dbo:
    # 初始化数据库操作
    def __init__(self):
        # 打开一个数据库连接
        # self.__db = pymysql.connect("localhost", "root", "admin123", "lianxiang", charset='utf8')
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

    # 插入BitMart交易对
    def insertExchangePair(self, createDate, lastUpdateDate, version, exchangeId, originalPair, baseCurrency,
                           quoteCurrency,
                           baseCurrencyId, exchangeName, exchangeUrl,open,originalPairId):
        sql = ""
        if (baseCurrencyId == -1):
            sql = "insert into b_exchange_pair(createDate_,lastUpdateDate_,version_,exchangeId_,originalPair_,baseCurrency_,quoteCurrency_,exchangeName_,exchangeUrl_,open_,originalPairId_) value(\"" + createDate + "\",\"" + lastUpdateDate + "\",%d,%d,%s,%s,%s,%s,%s,%d,%d)" %(version,exchangeId,"\""+originalPair+"\"","\""+baseCurrency+"\"","\""+quoteCurrency+"\"","\""+exchangeName+"\"","\""+exchangeUrl+"\"",open,originalPairId)
        else:
            sql = "insert into b_exchange_pair(createDate_,lastUpdateDate_,version_,exchangeId_,originalPair_,baseCurrency_,quoteCurrency_,baseCurrencyId_,exchangeName_,exchangeUrl_,open_,originalPairId_) value(\"" + createDate + "\",\"" + lastUpdateDate + "\",%d,%d,%s,%s,%s,%d,%s,%s,%d,%d)" %(version,exchangeId,"\""+originalPair+"\"","\""+baseCurrency+"\"","\""+quoteCurrency+"\"",baseCurrencyId,"\""+exchangeName+"\"","\""+exchangeUrl+"\"",open,originalPairId)
        try:
            self.__cursor.execute(sql)

            # 提交到数据库执行
            self.__db.commit()
        except:
            logging.exception("Exception Logged")
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

    def BitMart(self, url, exchangePair, exchangeName, exchangeId, exchangeUrl):
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
                    # 完整交易对
                    symbol = d[i]['pair']

                    # 基础币种
                    baseCurrency = str(symbol).split("_")[0]
                    # 计价币种
                    quoteCurrency = str(symbol).split("_")[1]

                    #原始交易对ID
                    symbolId = d[i]['symbolId']


                    flag = 1
                    for j in range(0, len(exchangePair)):
                        if (exchangePair[j][5] == symbol and exchangePair[j][4] == exchangeId):
                            flag = 0
                    if (flag == 1):

                        counts = counts + 1
                        nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        data = db.getEncryptedCurrency(baseCurrency)

                        if (data.__len__() == 0):
                            db.insertExchangePair(nowDate, nowDate, 1, exchangeId, symbol, baseCurrency,
                                                  quoteCurrency, -1, exchangeName, exchangeUrl,0,symbolId)
                        else:
                            baseCurrencyId = data[0][0]

                            db.insertExchangePair(nowDate, nowDate, 1, exchangeId, symbol, baseCurrency,
                                                  quoteCurrency, baseCurrencyId, exchangeName, exchangeUrl,0,symbolId)

                        print("数据库中未找到[%s]交易对,已入库" % symbol)
            print("已入库[%d]个交易对" % counts)
        except Exception as e:
            print("拉取BitMart交易对失败")
            print(e)


if __name__ == "__main__":
    db = dbo()
    # data = db.getEncryptedCurrency("btc")
    # print(data.__len__()>0)

    exchangePair = db.getExchangePair()
    db.BitMart("https://openapi.bitmart.com/tickers/market_cap", exchangePair,"BitMart",226,"https://www.bitmart.com/")
    print("BitMart交易对同步完毕")
