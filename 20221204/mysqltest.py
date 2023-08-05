import pymysql;


#mysql看看这个https://www.jianshu.com/p/4e72faebd27f

# mysql = {
#     "host": "192.168.8.34",
#     "user": "pingtt",
#     "password": "qwer1234",
#     "database": "large"
# }
mysql = {
    "host": "192.168.2.33",
    "user": "pingtt",
    "password": "qwer1234~!",
    "database": "pro_large"
}

db = pymysql.connect(host=mysql["host"], user=mysql["user"], port=3306, password=mysql["password"])
cursor = db.cursor()

def testmysql():
    sql = "SELECT * FROM `kylin`.`proofing_notice`"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            color_id = row[2]
            print(id, color_id)
    except:
        db.rollback()

# 写ding表的 remark 字段
def num_4():
    sql = "SELECT * FROM `ding`.`ding_employee`  where mobile is not null and remark is null "
    sql1 = "UPDATE `ding`.`ding_employee` SET remark = %s WHERE `id` = %s"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            id = row[0]
            mobile = row[7]
            remark1 = str(mobile[-4:])
            test1 = (remark1,id)
            print(test1)

            cursor.execute(sql1,test1)
        db.commit()
    except:
        db.rollback()


# 关闭数据库连接


if __name__ == '__main__':
    # testmysql()
    # num_4()
    db.close();
