import pymysql;

db = pymysql.connect(host='192.168.8.249', user='pingtt', port=3306, password='qwer1234~!')

cursor = db.cursor()
sql = "SELECT * FROM `exhibition`.`proofing_notice`"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        color_id = row[2]
        print(id, color_id)
except:
    db.rollback()

# 关闭数据库连接
db.close();

