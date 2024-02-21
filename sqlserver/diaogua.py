import pyodbc
# py链接sqlserver服务器
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.100.189,1433;DATABASE=jack;UID=sa;PWD=jack123')
print("数据库连接:", conn)
cur = conn.cursor()
if not cur:
    raise (NameError, "数据库连接失败")
cur.execute("SELECT  * from tColor")
resList = cur.fetchall()
conn.close()
print(resList)