import json

import pymysql;
import sqlite3
import pandas as pd


# 测试
mysql = {
    "host": "192.168.8.249",
    "user": "root",
    "password": "root",
    "database": "ding"
}


db = pymysql.connect(host=mysql["host"], user=mysql["user"], port=3306, password=mysql["password"])
cursor = db.cursor()





def depment():
    # 到底有哪些人扫码
    sql = "SELECT distinct a.user_id FROM `ding`.`canteen_person_scan_log` a "

    # 所有人员的部门组
    sql1 = "SELECT userid,depid,`order` FROM `ding`.`ding_employee_dep` a where a.userid = %s order by  a.`id`"

    #查询要修改的id
    sql3 = "SELECT a.id FROM `ding`.`canteen_person_scan_log` a where  a.user_id = %s"
    #写部门
    sql2 = "UPDATE `ding`.`canteen_person_scan_log` a SET a.depart = %s WHERE `id` = %s"

        # [[id,[11,11]],]
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            userid = row[0]
            cursor.execute(sql1,userid)
            results = cursor.fetchall()
            dep = []
            for row in results:
                userid = row[0]
                depid = row[1]
                order = row[2]
                print(order)
                if order == '0':
                    dep.insert(0,depid)
                else:
                    dep.append(depid)
            cursor.execute(sql3, userid)
            results1 = cursor.fetchall()
            for row in results1:
                id =row[0]
                array_as_json = json.dumps(dep)   #要转成json才能存
                test1=(array_as_json,id)
                print(test1)
                cursor.execute(sql2,test1)

        db.commit()
    except Exception as e:
        db.rollback(e)




if __name__ == '__main__':
    depment()