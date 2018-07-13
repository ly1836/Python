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

    # 查询所有K线分表名
    def selectAllKlineTableName(self, dbName):
        sql = "select table_name from information_schema.TABLES where table_name like '%b_exchange_pair_kline_%' and TABLE_SCHEMA='" + dbName + "'"
        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            return data
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()

    # 生成K线索引表数据
    def autoKlinTableIndexData(self,year):
        count = 0

        file = open("d:\\autoKlinTableIndexData.sql", "w")

        # 交易所ID
        exchangeId = {13, 28, 3, 4, 5, 6}

        # 月份(从6月开始,每月1号00:00:00时间戳)
        date = {6:1527782400000, 7:1530374400000, 8:1533052800000, 9:1535731200000, 10:1538323200000, 11:1541001600000, 12:1543593600000}

        # K线类型
        klineType = {"ONE_MINUTE", "THREE_MINUTE", "FIVE_MINUTE", "TEN_MINUTE", "FIFTEEN_MINUTE", "THIRTY_MINUTE",
                "SIXTY_MINUTE", "TWO_HOUR",
                "FOUR_HOUR", "SIX_HOUR", "TWELVE_HOUR", "ONE_DAY", "THREE_DAY", "ONE_WEEK", "ONE_MONTH"}

        for key in date:
            value = date[key]
            for i in exchangeId:
                for j in klineType:
                    lowerCase = str(j).lower()
                    print("exchangeId:%d --- ts:%d --- tableName:b_exchange_pair_kline_%d_%s_%s_%d" % (i,value,i,lowerCase,year,key))

                    file.write("insert into b_exchange_pair_kline(exchangeId_,type_,ts_,tableName_) values(%d,'%s',%d,'b_exchange_pair_kline_%d_%s_%s_%d');\n" % (i,str(j),value,i,lowerCase,year,key))
                    count = count + 1

        file.close()
        return count



if __name__ == "__main__":
    db = dbo()

    #tableName =  db.selectAllKlineTableName("quotation")

    count = db.autoKlinTableIndexData("2018")

    print("共生成[%d]条K线索引表数据" % count)

    #遍历字典
    # date = {6: 1527782400000, 7: 1530374400000, 8: 1533052800000, 9: 1535731200000, 10: 1538323200000,
    #         11: 1541001600000, 12: 1543593600000}
    # for key in date:
    #     print("%d:%d" % (key,date[key]))

