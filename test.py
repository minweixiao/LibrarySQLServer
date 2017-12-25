import pymssql

conn = pymssql.connect(host="127.0.0.1", port=1433,user="testLib", password="root", database="Library", charset="GBK")
str='本科生'
strstr
sql = "select readerTypeId from readertype where readerTypeName='本科生'"
#sql = "select readerTypeId from readertype"
print("---------")
cursor=conn.cursor()
print("*********")
# sql = "select readerTypeId from readertype where readerTypeName='本科生'"
cur=cursor.execute(sql)
print("----------+++++++++")
RTypeId = cursor.fetchall()
print("---------**********")
print(RTypeId)
# conn.commit()
conn.close()