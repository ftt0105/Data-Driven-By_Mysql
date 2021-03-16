#encoding=utf-8
import pymysql
from DatabaseInit import DataBaseInit

class MyMySQL(object):
    def __init__(self, host, port, dbName, username, password, charset):
        # 进行数据库初始化
        dbInit = DataBaseInit(host, port, dbName, username, password, charset)
        dbInit.create()
        dbInit.insertDatas()
        self.conn = pymysql.connect(
            host = host,
            port = port,
            db = dbName,
            user = username,
            passwd = password,
            charset = charset
        )
        self.cur = self.conn.cursor()

    def getDataFromDataBases(self):
        # 从testdata表中获取需要的测试数据
        # bookname作为搜索关键词，author作为预期关键词
        self.cur.execute("select bookname, author from testdata;")
        # 从查询区域取回所有查询结果
        datasTuple = self.cur.fetchall()
        return datasTuple

    def closeDatabase(self):
        # 数据库后期清理工作
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    db = MyMySQL(
        host="localhost",
        port=3306,
        dbName="gloryroad",
        username="root",
        password="gloryroad",
        charset="utf8"
    )
    print (db.getDataFromDataBases())
