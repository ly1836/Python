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


    # -------------------------爬取代理地址开始--------------------------------
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

    # -------------------------爬取代理地址开始--------------------------------


    #-------------------------人物表操作开始-----------------------------------
    '''
        <p>
            插入人物
        </p>
        @name 人物名
        @img 图片地址
        @alias 用于当前人物查询fanhao地址
    '''
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



    '''
        获取所有人物信息
    '''
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


    # -------------------------fanhao表操作开始--------------------------------
    '''
        <p>
            插入fanhao资源并且在关联表中插入关联关系
        </p>
        @designation fanhao
        @img 图片地址
        @figureId 人物ID
    '''
    def insertFigureSource(self, designation, img,date, figureId):
        sql = "insert into source(designation,img_src,date) VALUE(\"" + designation + "\",\"" + img+ "\",\"" + date + "\")"

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

    # -------------------------fanhao表操作结束--------------------------------



    # -------------------------磁力链接表操作开始--------------------------------

    '''
        <p>
            插入磁力链接
        </p>
        @create_time 创建时间.
        @file_size 文件大小
        @magnet_link 磁力链接
        @thunder_link 迅雷链接
        @source_id 番号ID
    '''
    def insertMagent(self,create_time,file_size,magnet_link,source_id):
        sql = "insert into magnet(create_time,file_size,magnet_link) VALUE(\"" + create_time + "\",\"" + file_size + "\",\"" + magnet_link+  "\")"

        try:
            self.__cursor.execute(sql)

            # 最新插入行的主键ID
            magentId = self.__db.insert_id()

            # 在磁力fanhao关联表中插入关联
            sql = "insert into source_magnet(magnet_id,source_id) VALUE(%d,%d)" % (magentId, source_id)

            self.__cursor.execute(sql)

            # 提交到数据库执行
            self.__db.commit()
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
            self.__db.close()


    '''
        <p>
            获取数据库中所有fanhao
        </p>
    '''
    def getAllSource(self,id):
        sql = "select *from source where id > %d" % id

        try:
            self.__cursor.execute(sql)

            data = self.__cursor.fetchall()

            return data
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

    #db.insertMagent("2017-7-7","1.6 GB","magnet:?xt=urn:btih:2efc513819c1314e409bd893a684d60c0baed3d3","thunder://QUFtYWduZXQ6P3h0PXVybjpidGloOjJlZmM1MTM4MTljMTMxNGU0MDliZDg5M2E2ODRkNjBjMGJhZWQzZDNaWg==",1)

    data = db.getAllSource()
    print(data)
