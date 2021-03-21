import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pymysql
from common.dbConfig import dbConfig
from model.UserSet import initMessageQue

class conn:
    rds = pymysql.connect(
        user=dbConfig.USER[0],
        passwd=dbConfig.PASSWD[0],
        port=dbConfig.PORT[0],
        host=dbConfig.HOST[0],
        db=dbConfig.DB,
        charset='utf8'
    )

    def disableTalk(entity):
        cursor = conn.rds.cursor(pymysql.cursors.DictCursor)
        columns = ','.join(entity.keys())
        query = "UPDATE %s SET Work = 0 WHERE id = '%s'" % (dbConfig.KAKAOTABLE, entity['id'])
        print(query)
        cursor.execute(query)
        conn.rds.commit()

    def addData(entity):
        cursor = conn.rds.cursor(pymysql.cursors.DictCursor)
        columns = ','.join(entity.keys())
        query = "INSERT INTO %s (%s) VALUES %s ON DUPLICATE KEY UPDATE location = '%s', time = '%s', work = 1 " % (dbConfig.KAKAOTABLE, columns, '(%s, %s, %s, %s, %s)', entity['location'], entity['time'])
        value = tuple(_ for _ in entity.values())
        print(query)
        print(value)
        cursor.execute(query, value)
        conn.rds.commit()

    def getData(time):
        cursor = conn.rds.cursor(pymysql.cursors.DictCursor)
        query = ('SELECT * FROM ( SELECT ROW_NUMBER() OVER(PARTITION BY id ORDER BY created DESC) AS RN, id, location, time, work, created FROM  %s ) AS TBL WHERE RN = 1 AND work = 1 AND time = %s' % (dbConfig.KAKAOTABLE, time))
        print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        return rows

    def getAll():
        cursor = conn.rds.cursor(pymysql.cursors.DictCursor)
        sql = ('SELECT * FROM %s' % (dbConfig.KAKAOTABLE))
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            print(i)
        return result

    def getMessageQue(startTime, endTime):
        cursor = conn.rds.cursor(pymysql.cursors.DictCursor)
        sql = ("SELECT id, location FROM %s WHERE work = 1 AND time BETWEEN '%s' AND '%s' " % (dbConfig.KAKAOTABLE, startTime, endTime))
        cursor.execute(sql)
        result = cursor.fetchall()
        data = []
        for i in result:
            row = initMessageQue(i)
            data.append(row)
        return data
    


