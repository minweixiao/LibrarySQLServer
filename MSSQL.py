import pymssql
import time

reader = "1"
book="1"
borrowInfo="1"
book_insert="1"
reader_inert="1"
class MSSQL(object):
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd,database=self.db , charset="GBK")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        if resList!=None:
            return resList
        return "success"

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
    # ---------------------------------------------------------------------
    # 查询读者和获取读者
    def readerQuery(self):
        global reader
        reader=self.ExecQuery("select * from View_Reader")
        # print(reader)
        return reader
    def getReader(self):
        rea=self.readerQuery()
        # print(rea)
        return rea
    # 查询图书和获取图书
    def bookQuery(self):
        global book
        book=self.ExecQuery("select * from View_Book")
        return book
    def getBook(self):
        boo=self.bookQuery()
        return boo
    def bookOneQuery(self,bookId):
        global book
        sql="select * from View_Book where bookId="+str(bookId)
        print(sql)
        book0=self.ExecQuery(sql)
        print(book0)
        return book0
    def getOneBook(self,bookId):
        boo = self.bookOneQuery(bookId)
        return boo
    # 模糊查询
    def bookQuery_mohu(self,sql):
        book_mohu=self.ExecQuery(sql)
        return book_mohu
    # 查询记录和获取记录
    def BorrowInfoQuery(self):
        global borrowInfo
        borrowInfo=self.ExecQuery("select * from View_Borrow")
        return borrowInfo
    def getBorrowInfo(self):
        borrowIn=self.BorrowInfoQuery()
        return borrowIn
    # 插入图书
    def bookInsert(self,bName,bISBN,bAuthor,bNum,bPublisher,bPrice,bType):
    # def bookInsert(self):
        global book_insert
        if bType=="CS":
            typeId="1"
        if bType=="literature":
            typeId="2"
        if bType=="philosophy":
            typeId="3"
        # book_insert=self.ExecQuery("")
        # sql = "insert into book(pwd,name,phone,email,readerTypeId) VALUES ('" + Rpwd + "','" + Rname + "','" + Rphone + "','" + Remail + "'," + readerTypeId0 + ")"
        sql="exec insertBook @bookName='"+bName+"',@ISBN='"+bISBN+"',@autho='"+bAuthor+"',@num="+bNum+",@press='"+bPublisher+"',@price="+bPrice+",@typeId="+typeId
        print(sql)
        book_insert=self.ExecNonQuery(sql)
        return book_insert
    # 插入读者
    def readerInsert(self,Rname,Rpwd,Rphone,Remail,RTypeName):
        # global reader_inert
        print("-----")
        # sql="select readerTypeName from readertype where readerTypeId=1"
        # print(sql)
        # readerTypeId0=self.ExecQuery(sql)
        # print(readerTypeId0)
        if RTypeName=="本科生":
            readerTypeId0="1"
        if RTypeName=="研究生":
            readerTypeId0="2"
        if RTypeName=="教师":
            readerTypeId0="3"
        # Rname=Rname.encode('gbk')
        # unicode(Rname, "gbk")
        sql="insert into reader(pwd,name,phone,email,readerTypeId) VALUES ('"+Rpwd+"','"+Rname+"','"+Rphone+"','"+Remail+"',"+readerTypeId0+")"
        print(sql)
        reader_inert=self.ExecNonQuery(sql)
        print("**********")
        return reader_inert

    def userOneQuery(self,userId):
        global book
        sql="select * from View_Reader where readerId="+str(userId)
        print(sql)
        user0=self.ExecQuery(sql)
        return user0

    def getOneUser(self,userId):
        use = self.userOneQuery(userId)
        return use

    def userOneUpdate(self,sql):
        self.ExecNonQuery(sql)

    def bookOneUpdate(self,sql):
        self.ExecNonQuery(sql)

    # 插入记录
    def borrowInfoInsert(self, sql):
        # global reader_inert
        reader_inert = self.ExecQuery(sql)
        # print(reader_inert)
        print("**********")
        return reader_inert

    # 删除读者
    def deleteReader(self,userId):
        sql="delete from reader where readerid="+userId
        print(sql)
        self.ExecNonQuery(sql)
        # print(reader_delete)

    # 删除图书
    def deleteBook(self, bookId):
        # sql="select from borrowinfo where bookId="+bookId
        # mess=self.ExecQuery(sql)
        # print(mess)
        sql = "delete from book where bookId=" + bookId
        print(sql)
        self.ExecNonQuery(sql)
        # print(reader_delete)

    # 备份
    def database_beifen(self):
        # sql="BACKUP DATABASE Library TO DISK = 'D:\\sql server\\database.bak'"
        # print(sql)
        # self.ExecNonQuery(sql)
        # print("-----------")
        # # print(thing)
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ""

        con = pymssql.connect(host='127.0.0.1', port='1433', user='sa', password='root', database='Library')
        con.autocommit(True)
        cur = con.cursor()
        sql = "BACKUP DATABASE Library TO DISK ='D:/sql server/Library_" + nowtime + ".bak'"
        print(sql)
        cur.execute(sql)
        con.autocommit(False)
        cur.close()

    def database_huanyuan(self):
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ""
        con = pymssql.connect(host='127.0.0.1', port='1433', user='sa', password='root', database='Library')
        con.autocommit(True)
        cur = con.cursor()
        sql = "USE master RESTORE FILELISTONLY FROM DISK = 'D:/sql server/Library_2017-12-22-15-18-07' Go "
        print(sql)
        cur.execute(sql)
        con.autocommit(False)
        cur.close()



    # def bookQuery(self):
    #     global book
    #     book=self.ExecQuery("select * from book")
    #     return book
    # def getBook(self):
    #     boo=self.bookQuery()
    #     return boo

# # if __name__ == '__main__':
# #     MSSQL.main(self)
# print("001")
# # resList = ms.ExecQuery("insert into book values(100004,'计算机组成原理',1111,'唐说非',1,1,'高等教育出版社',43.0,1)")
# resList1=ms.ExecQuery("select * from book")
# resList2=ms.ExecQuery("select * from admin")
#
# print("002")
# print(resList1)
# reader=ms.ExecQuery("select * from reader")
# ms = MSSQL(host="127.0.0.1:1433", user="sa", pwd="root", db="Library")
# print(ms.getReader())
# print(ms.getBook())