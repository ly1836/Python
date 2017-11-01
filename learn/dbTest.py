
#测试数据库操作
import logging

import pymysql

class MysqlCon:

    #初始化数据库操作
    def __init__(self):
        # 打开一个数据库连接
        self.__db = pymysql.connect("localhost","root","admin","pydb",charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.__cursor = self.__db.cursor()

        print("数据库连接已建立")

    #获取user表中所有用户
    def getAllUser(self):
        # 使用 execute()  方法执行 SQL 查询
        self.__cursor.execute("select * from user")

        # 使用 fetchone() 方法获取数据
        data = self.__cursor.fetchall()

        print("id--姓名--性别--年龄")
        for x in data:
            print(x)

        # 关闭数据库连接
        self.__db.close()

    #插入用户
    def addUser(self):
        sql = "insert into user(name,sex,age) VALUE('王五',12,'123')"

        try:
            i =0
            # 执行sql语句
            while True:
                if i > 100000:
                    break
                self.__cursor.execute(sql)
                i+=1

            # 提交到数据库执行
            self.__db.commit()
            print("数据插入成功")
        except:
            logging.exception("Exception Logged")
            self.__db.rollback()
            print("数据库操作出错,事物已回滚")
        finally:
            self.__db.close()

            print("关闭数据库连接")

if __name__ == "__main__":
    x = MysqlCon()
    # 获取user表中所有用户
    x.getAllUser()
    #插入用户
    #x.addUser()


