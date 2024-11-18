import pymysql;
import pandas as pd

# mysql看看这个https://www.jianshu.com/p/4e72faebd27f

# mysql = {
#     "host": "192.168.8.34",
#     "user": "pingtt",
#     "password": "qwer1234",
#     "database": "large"
# }
# 正式
mysql = {
    "host": "192.168.2.33",
    "user": "pingtt",
    "password": "qwer1234~!",
    "database": "pro_large"
}
# 测试
# mysql = {
#     "host": "192.168.8.249",
#     "user": "root",
#     "password": "root",
#     "database": "exhibition"
# }


db = pymysql.connect(host=mysql["host"], user=mysql["user"], port=3306, password=mysql["password"])
cursor = db.cursor()


def Explmysql():
    sql = "SELECT a.id,g.name,c.name,d.qa_time FROM exhibition.proofing_notice as a" \
          " LEFT join exhibition.deve_color as b on a.color_id = b.id " \
          " LEFT JOIN exhibition.basic_config as c on b.place_id = c.id" \
          " LEFT JOIN exhibition.proofing_notice_nodedate as d on a.id = d.notice_id" \
          " LEFT JOIN exhibition.pub_samtypes g on g.id = a.properties_id " \
          " WHERE a.flag = 0 and a.deleted_at is null  and a.properties_id=1 AND b.place_id = 339 and a.nuclear_date BETWEEN '2023-08-01' AND '2023-08-15' " \
          "and a.area_id = 1 "

    sql1 = ""

    qaarray = []

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        for row in results:
            id = row[0]
            place_id = row[1]
            name = row[2]
            qatime = row[3]
            # print(id, place_id, name)
            qaarray.append(qatime)
            print(qaarray)
    except:
        db.rollback()

    avgqa = sum(qaarray) / len(qaarray)
    print(avgqa)


# 写ding表的 remark 字段
def Dingnum_4():
    # 补公司的wifi
    sql = "SELECT * FROM `ding`.`ding_employee`  where mobile is not null and remark is null and status = 1"
    sql1 = "UPDATE `ding`.`ding_employee` SET remark = %s WHERE `id` = %s"
    # 默认生产基地为1
    sql2 = "SELECT * FROM `ding`.`ding_employee`  where place_from is null and status = 1"
    sql3 = "UPDATE `ding`.`ding_employee` SET place_from = %s WHERE `id` = %s"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            id = row[0]
            mobile = row[7]
            remark1 = str(mobile[-4:])
            test1 = (remark1, id)
            print(test1)

            cursor.execute(sql1, test1)
        db.commit()
    except:
        db.rollback()

    try:
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            place_from = 1
            test2 = (place_from, id)
            cursor.execute(sql3, test2)
        db.commit()
    except:
        db.rollback()

# 主要删除一些软删的数据
def weihu():
    sql = "SELECT id FROM `kylin`.`proofing_notice_plan_less` a  WHERE a.deleted_at is not null "
    sql1 = "DELETE FROM `kylin`.`proofing_notice_plan_less`  WHERE `id` = %s"
    try:

        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            print(id)
            cursor.execute(sql1, id)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


# 批量处理excel中报废设备
def zicanbaofei():
    df = pd.read_excel('111.xlsx')
    column_data = df['编码'].values.tolist()
    # print(column_data)

    sql = "SELECT a.code FROM `kylin`.`equipment` as a"
    sql1 = "UPDATE `kylin`.`equipment` SET  `status` = 5 WHERE `code` = %s"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            code = row[0]

            if code in column_data:
                print(code);
                cursor.execute(sql1, code)
        db.commit()
    except Exception as e:
        db.rollback()



if __name__ == '__main__':
    # Explmysql();
    Dingnum_4();
    weihu();
    # zicanbaofei();

    # 关闭数据库连接
    db.close();
