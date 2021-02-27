import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pymysql
from common.dbConfig import dbConfig

class conn:
    rds = pymysql.connect(
        user=dbConfig.USER[0],
        passwd=dbConfig.PASSWD[0],
        port=dbConfig.PORT[0],
        host=dbConfig.HOST[0],
        db=dbConfig.DB,
        charset='utf8'
    )

    def addData(entity):
        cursor = conn.rds.cursor(pymysql.cursors.DictCursor)
        columns = ','.join(entity.keys())
        query = 'INSERT INTO %s (%s) VALUES %s ' % (dbConfig.KAKAOTABLE, columns, '(%s, %s, %s, %s, %s)')
        value = tuple(_ for _ in entity.values())
        print(query)
        print(value)
        cursor.execute(query, value)
        conn.rds.commit()

    def getAll():
        cursor = rds.cursor(pymysql.cursors.DictCursor)
        sql = ('SELECT * FROM %s' % (dbConfig.KAKAOTABLE))
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            print(i)
        return result
    


