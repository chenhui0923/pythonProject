import pymysql;
mysql = {
    "host": "192.168.8.249",
    "user": "pingtt",
    "password": "qwer1234~!",
    "database": "large"
}
# mysql = {
#     "host": "192.168.2.33",
#     "user": "pingtt",
#     "password": "toprich",
#     "database": "pro_large"
# }

db = pymysql.connect(host=mysql["host"], user=mysql["user"], port=3306, password=mysql["password"])


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

