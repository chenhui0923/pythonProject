import pyodbc  # py链接sqlserver服务器
import pymysql;  # py链接mysql服务器
from datetime import  datetime





conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.100.190,1433;DATABASE=LDEXCH;UID=sa;PWD=jack123')
db = pymysql.connect(host='192.168.9.220', user='middle', port=3306, password='middle')


cur = conn.cursor()
cursor = db.cursor()


if not cur:
    raise (NameError, "数据库连接失败")


def diaogua_190():
    sql = "SELECT  * from tOWorkSum where WorkLine=103"

    try:
        cur.execute(sql)
        resList = cur.fetchall()
        for row in resList:
            ShtDate = row[1]    # 生产日期
            IsOT    = row[2]    # 加班否
            MONo    = row[3]    # 款号
            ColorNo = row[7]    #色号
            SeqNo   = row[12]   #工序序号
            SeqName = row[14]  #工序名称
            Qty     = row[24]   #数量
            WorkLine =  row[19] #哪个工作站
            text1= (ShtDate,IsOT,MONo,ColorNo,SeqNo,SeqName,Qty,WorkLine)
            print(text1)
        conn.commit()
    except:
        conn.rollback()


def jishudiaogua_220():
    sql = "SELECT process_date,style_no,color,size,process_name,staff_name,quantity FROM middle.dg_daily_record a where a.process_last=1 and a.process_date='2024-04-10'"
    shuzu=[]
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            process_date = row[0]   #日期
            style_no = row[1]       #款号
            color = row[2]          #色号
            size = row[3]           #尺码
            process_name = row[4]   #工序名
            staff_name = row[5]     #操作员
            quantity = row[6]       #数量
            day = process_date.strftime('%Y%m%d')
            test1 = (day,style_no,color,size,process_name,staff_name,quantity)
            # shuzu.append(test1)
            print(test1)
        db.commit()
    except:
        db.rollback()







if __name__ == '__main__':
    # diaogua_190();
    jishudiaogua_220();

    conn.close()
