import pandas as pd
# 要先执行以下命令才能玩   后面的是项目的文件路径
# pip install pandas --target=D:\pythonProject\venv\Lib\site-packages
# pip install Pyarrow --target=D:\pythonProject\venv\Lib\site-packages
# pip install openpyxl --target=D:\pythonProject\venv\Lib\site-packages

# 学习https://c.biancheng.net/pandas/excel.html

def writeExcel():
#创建DataFrame数据
     info_website = pd.DataFrame({'名称': ['编程帮', 'c语言中文网', '微学苑', '92python'],
          '等级': [1, 2, 3, 4],
          '语言': ['PHP', 'C', 'PHP','Python' ],
          '网址': ['www.bianchneg.com', 'c.bianchneg.net', 'www.weixueyuan.com','www.92python.com' ]})
     #创建ExcelWrite对象
     writer = pd.ExcelWriter('website.xlsx')
     info_website.to_excel(writer)
     writer.close()
     print('输出成功')

def readExcel():
     df = pd.read_excel('website.xlsx',index_col='名称')
     df.columns = df.columns.str.replace('Unnamed: 0', '序号')
     print(df)



writeExcel()
# readExcel()