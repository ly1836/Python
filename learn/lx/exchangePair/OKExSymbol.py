import json
import requests
import pymysql
import logging
import datetime


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

    # 插入okex交易对
    def insertExchangePair(self, createDate, lastUpdateDate, version, exchangeId, originalPair, baseCurrency,
                           quoteCurrency,
                           baseCurrencyId, exchangeName, exchangeUrl,open):
        sql = ""
        if (baseCurrencyId == -1):
            sql = "insert into b_exchange_pair(createDate_,lastUpdateDate_,version_,exchangeId_,originalPair_,baseCurrency_,quoteCurrency_,exchangeName_,exchangeUrl_,open_) value(\"" + createDate + "\",\"" + lastUpdateDate + "\",%d,%d,%s,%s,%s,%s,%s,%d)" %(version,exchangeId,"\""+originalPair+"\"","\""+baseCurrency+"\"","\""+quoteCurrency+"\"","\""+exchangeName+"\"","\""+exchangeUrl+"\"",open)
        else:
            sql = "insert into b_exchange_pair(createDate_,lastUpdateDate_,version_,exchangeId_,originalPair_,baseCurrency_,quoteCurrency_,baseCurrencyId_,exchangeName_,exchangeUrl_,open_) value(\"" + createDate + "\",\"" + lastUpdateDate + "\",%d,%d,%s,%s,%s,%d,%s,%s,%d)" %(version,exchangeId,"\""+originalPair+"\"","\""+baseCurrency+"\"","\""+quoteCurrency+"\"",baseCurrencyId,"\""+exchangeName+"\"","\""+exchangeUrl+"\"",open)
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

    def okex(self, url, exchangePair):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'upgrade-insecure-requests':'1',
            'pragma':'no-cache',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'no-cache',
            'cookie':'__cfduid=d758306b7a20b60b97e9dce01b629bff71528790848; locale=zh_CN; perm=AEB726BADDCF76C2EAFEE980B2117699; lp=; _ga=GA1.2.1165342718.1528790875; Hm_lvt_b4e1f9d04a77cfd5db302bc2bcc6fe45=1530084291,1530254260,1530504420,1530819782'
        }

        proxies = {'https': '127.0.0.1:1080'}
        try:

            respone = requests.get(url, headers=headers,proxies=proxies)

            if respone.text.__len__() > 1:
                d = json.loads(respone.text)['data']
                for i in range(1, len(d)):
                    flag = 1
                    for j in range(1, len(exchangePair)):
                        if (exchangePair[j][5] == d[i]['symbol'] and exchangePair[j][4] == 6):
                            flag = 0
                    if (flag == 1):
                        nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        baseCurrency = (d[i]['symbol'] + "")[0:((d[i]['symbol'] + "").index("_"))]
                        quoteCurrency = (d[i]['symbol'] + "")[
                                        (d[i]['symbol'] + "").index("_") + 1:len(d[i]['symbol'] + "")]
                        data = db.getEncryptedCurrency(baseCurrency)

                        if (data.__len__() == 0):
                            db.insertExchangePair(nowDate, nowDate, 1, 6, d[i]['symbol'], baseCurrency,
                                                  quoteCurrency, -1, "OKEX", "https://www.okex.com",0)
                        else:
                            baseCurrencyId = data[0][0]

                            db.insertExchangePair(nowDate, nowDate, 1, 6, d[i]['symbol'], baseCurrency,
                                                  quoteCurrency, baseCurrencyId, "OKEX", "https://www.okex.com",0)

                        print("数据库中未找到[%s]交易对,已入库" % d[i]['symbol'])

        except Exception as e:
            print("拉取okex交易对失败")
            print(e)


if __name__ == "__main__":
    db = dbo()
    # data = db.getEncryptedCurrency("btc")
    # print(data.__len__()>0)

    exchangePair = db.getExchangePair()
    db.okex("https://www.okex.com/v2/spot/markets/products", exchangePair)
    print("OKEX交易所交易对同步完毕")
