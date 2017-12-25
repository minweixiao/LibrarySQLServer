import pymssql
from flask import Flask, request, render_template
from MSSQL import *
app = Flask(__name__)
reader=" "
book=" "
oneBook=" "
borrowInfo=" "
ms=" "
userId=" "
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#-------------------------------------------------------------------------------
# ********************
# 管理员登录
@app.route('/adminLogin.html', methods=['GET', 'POST'])
def adminLogin():
    return render_template('adminLogin.html')

@app.route('/adminLogin', methods=['POST','GET'])
def adminLogin02():
    aName=request.form['aName']
    aPassword=request.form['aPassword']
    if aPassword=="hello":
        return render_template('index.html')

# 管理员登录
@app.route('/userLogin.html', methods=['GET', 'POST'])
def userLogin():
    return render_template('userLogin.html')

@app.route('/userLogin', methods=['POST','GET'])
def userLogin02():
    aName=request.form['aName']
    aPassword=request.form['aPassword']
    if aPassword=="hello":
        return render_template('user.html')

# ********************
# 查看个人资料
@app.route('/my-profile.html', methods=['GET', 'POST'])
def my_profile():
    return render_template('my-profile.html')
# ----------------------------------------------------------------------
# ********************
# 初始化读者界面
@app.route('/new-reader.html', methods=['GET','POST'])
def new_user():
    return render_template('new-reader.html')

# ********************
# 新建读者
@app.route('/new-reader', methods=['POST'])
def new_user1():
    global ms
    rName=request.form['rName'];
    rPhone = request.form['rPhone'];
    rEmail = request.form['rEmail'];
    rPwd = request.form['rPwd'];
    rRole = request.form['rRole'];
    # sql_newBook="USE [Library] EXEC [dbo].[insertStudent]@name='"+rName+"',@phone='"+rPhone+"',@email='"+rEmail+"',@pwd='"+rPwd+"',@readerTypeName='"+rRole+"'"
    # print(sql_newBook)
    # print(ms)
    # ms.readerInsert()
    # print(reader_inert)
    thin=ms.readerInsert(rName,rPwd,rPhone,rEmail,rRole)
    print(thin)
    return render_template('index.html')

# ********************
# 管理读者
@app.route('/reader.html', methods=['GET', 'POST'])
def reader():
    global ms
    reader=ms.getReader()
    return render_template('reader.html',reader=reader)

# ********************
# 管理读者
@app.route('/reader', methods=['GET','POST'])
def reader01():
    global ms
    global userId
    userId=request.form['userId']
    print(userId)
    oneUser = ms.getOneUser(userId)
    print(oneUser)
    return render_template('update-reader.html',oneUser=oneUser)

# ********************
# 更新读者信息
@app.route('/update-reader', methods=['POST','GET'])
def reader02():
    global ms
    global userId
    rName=request.form['rName']
    rPhone = request.form['rPhone']
    rEmail = request.form['rEmail']
    rRole = request.form['rRole']

    print(rName)
    sql="update reader set name='"+rName+"' where readerId="+userId
    ms.userOneUpdate(sql)
    return render_template('reader.html')

# ********************
# 删除读者信息
@app.route('/delete-reader', methods=['POST','GET'])
def reader03():
    global ms
    userId=request.form['userId']
    ms.deleteReader(userId)
    oneUser = ms.getOneUser(userId)
    print(oneUser)
    return render_template('reader.html')

# ---------------------------------------------------------------------------
# ********************
# 初始化图书界面
@app.route('/new-book.html', methods=['GET', 'POST'])
def new_book():
    # bookName = request.form['bookName']
    # ISBN = request.form['ISBN']
    # num = request.form['num']
    # press = request.form['press']
    # price = request.form['price']
    return render_template('new-book.html')

# ********************
# 新建读者
@app.route('/new-book', methods=['POST'])
def new_book1():
    global ms
    bName=request.form['bName'];
    bISBN = request.form['bISBN'];
    bAuthor = request.form['bAuthor'];
    rNum = request.form['rNum'];
    bPublisher = request.form['bPublisher'];
    bPrice = request.form['bPrice'];
    bType = request.form['bType'];
    # sql_newBook="USE [Library] EXEC [dbo].[insertStudent]@name='"+rName+"',@phone='"+rPhone+"',@email='"+rEmail+"',@pwd='"+rPwd+"',@readerTypeName='"+rRole+"'"
    # print(sql_newBook)
    # print(ms)
    # ms.readerInsert()
    # print(reader_inert)
    thin=ms.bookInsert(bName,bISBN,bAuthor,rNum,bPublisher,bPrice,bType)
    print(thin)
    return render_template('index.html')

# ********************
# 新建读书
@app.route('/book', methods=['POST'])
def book01():
    global ms
    # print(type(request.form['userId']))
    bookId=request.form['bookId']
    print(bookId)
    # print(ms)
    oneBook=ms.getOneBook(bookId)
    print(oneBook)
    return render_template('update-book.html',oneBook=oneBook)

# ********************
# 管理图书
@app.route('/book.html', methods=['POST','GET'])
def book():
    global ms
    book = ms.getBook()
    return render_template('book.html',book=book)

# ********************
# 更新图书信息
@app.route('/update-book', methods=['POST','GET'])
def book02():
    global ms
    bId=request.form['bId']
    bName=request.form['bName']
    bPublisher = request.form['bPublisher']
    bPrice = request.form['bPrice']
    bAuthor = request.form['bAuthor']

    # print(bName)
    sql = "update book set bookName='" + bName + "' where bookId=" + bId
    use=ms.bookOneUpdate(sql)
    return render_template('reader.html')

# ********************
# 删除图书信息
@app.route('/delete-book', methods=['POST','GET'])
def book03():
    global ms
    bookId=request.form['bookId']
    ms.deleteBook(bookId)
    # oneUser = ms.getOneUser(userId)
    # print(oneUser)
    return render_template('book.html')
# -----------------------------------------------------------------------------
# ********************
# 初始化借阅界面
@app.route('/new-borrow.html', methods=['GET', 'POST'])
def new_borrow():
    return render_template('new-borrow.html')

# ********************
# 借阅管理
@app.route('/borrow.html', methods=['GET', 'POST'])
def borrow():
    global borrowInfo
    return render_template('borrow.html',borrowInfo=borrowInfo)

@app.route('/visitor.html', methods=['GET', 'POST'])
def visitor():
    return render_template('visitor.html')

@app.route('/visitor', methods=['POST','GET'])
def visitor1():
    global ms
    bName=request.form['bName']
    print(bName)
    sql="select * from book where bookName like'%"+bName+"%'"
    book_mohu=ms.bookQuery_mohu(sql)
    print(book_mohu)
    return render_template('visitor.html',book_mohu=book_mohu)


@app.route('/user.html', methods=['GET', 'POST'])
def user():
    return render_template('user.html')

@app.route('/user', methods=['POST','GET'])
def user1():
    global ms
    bName=request.form['bName']
    print(bName)
    print("user")
    sql="select * from book where bookName like'%"+bName+"%'"
    book_mohu=ms.bookQuery_mohu(sql)
    print(book_mohu)
    return render_template('user.html',book_mohu=book_mohu)


@app.route('/borrow01', methods=['POST'])
def borrow01():
    global ms
    bookId=request.form['bookId']
    print(bookId)
    # sql="select * from book where bookName like'%"+bName+"%'"
    # book_mohu=ms.bookQuery_mohu(sql)
    # print(book_mohu)
    return render_template('user.html')

@app.route('/database', methods=['POST','GET'])
def database():
    global ms
    da=request.form['data']
    print(da)
    ms.database_beifen()
    return render_template('index.html')

@app.route('/database_huanyuan', methods=['POST','GET'])
def database_huanyuan():
    global ms
    # da=request.form['data']
    # print(da)
    ms.database_huanyuan()
    return render_template('index.html')



def getInfo():
    global book
    global borrowInfo
    global ms
    ms = MSSQL(host="127.0.0.1:1433", user="testLib", pwd="root", db="Library")
    # ms.database_beifen()
    # ms.bookInsert()
    # print(ms)
    # book=ms.getBook()
    # borrowInfo=ms.getBorrowInfo()
    # ms.bookOneQuery("100002")
    # ms.readerInsert()
    # print("132")
    # reader_inert = ms.readerInsert('uu','1','1','1','1')
    # print("789")
    # print(reader_inert)
if __name__ == '__main__':
    # print("1")
    getInfo()
    # print("2")
    app.run()
    print("3")

