import pymysql
import logging


class dbo:
    # 初始化数据库操作
    def __init__(self):
        # 打开一个数据库连接
        self.__db = pymysql.connect("localhost", "root", "admin", "pydb", charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.__cursor = self.__db.cursor()

        print("数据库连接已建立")

    # 保存爬取到代理IP及port
    def saveProxy(self, ip, port, types):
        sql = "insert into proxy(ip,port,type) VALUE(\"" + ip + "\",\"" + port + "\",\"" + types + "\")"

        try:
            self.__cursor.execute(sql)

            # 提交到数据库执行
            self.__db.commit()
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()

    # 获取前n条数据
    def getProxyByNum(self, n):
        sql = "select * from proxy limit " + n + ""

        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            for x in data:
                print(x)
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()
        pass

    #-------------------------人物表操作开始--------------------------------
    # 插入人物
    def insertFigure(self, name, img, alias):
        sql = "insert into figure(name,img_src,alias) VALUE(\"" + name + "\",\"" + img + "\",\"" + alias + "\")"

        try:
            self.__cursor.execute(sql)

            # 提交到数据库执行
            self.__db.commit()
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()



    #获取所有人物信息
    def getAllFigure(self):
        sql = "select *from figure"

        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            return data
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()



    # -------------------------人物表操作结束--------------------------------

    def insertFigureSource(self, designation, img, figureId):
        sql = "insert into source(designation,img_src) VALUE(\"" + designation + "\",\"" + img + "\")"

        try:
            self.__cursor.execute(sql)

            # 最新插入行的主键ID
            soureId = self.__db.insert_id()

            #在人物fanhao关联表中插入关联
            sql = "insert into figure_source(figure_id,source_id) VALUE(%d,%d)" % (figureId, soureId)

            self.__cursor.execute(sql)

            # 提交到数据库执行
            self.__db.commit()
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()


if __name__ == "__main__":
    db = dbo()
    # db.saveProxy("127.0.0.1", "8080", "http")
    # db.getProxyByNum("10")
    #db.insertFigureSource("apc-1", "http://www.test.com/img.jpg", 1)

    data = db.getAllFigure()
    print(data[0])
