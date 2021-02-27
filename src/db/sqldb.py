import pymysql

rds = pymysql.connect(
    user='sa',
    passwd='',
    port=9,
    host='',
    db='',
    charset='utf8'
)

cursor = rds.cursor(pymysql.cursors.DictCursor)
sql = 'SELECT * FROM tbl_'
cursor.execute(sql)
result = cursor.fetchall()
print(result)
