import pandas as pd
# 要先执行以下命令才能玩   后面的是项目的文件路径
# pip install pandas --target=D:\pythonProject\venv\Lib\site-packages
# pip install Pyarrow --target=D:\pythonProject\venv\Lib\site-packages
# pip install openpyxl --target=D:\pythonProject\venv\Lib\site-packages



def writeExcel():
#创建DataFrame数据
     info_website = pd.DataFrame({'name': ['编程帮', 'c语言中文网', '微学苑', '92python'],
          'rank': [1, 2, 3, 4],
          'language': ['PHP', 'C', 'PHP','Python' ],
          '': ['www.bianchneg.com', 'c.bianchneg.net', 'www.weixueyuan.com','www.92python.com' ]})
     #创建ExcelWrite对象
     writer = pd.ExcelWriter('website.xlsx')
     info_website.to_excel(writer)
     writer.close()
     print('输出成功')

def readExcel():
     df = pd.read_excel('website.xlsx',index_col='name')
     df.columns = df.columns.str.replace('Unnamed: 0', 'col_label')
     print(df)

# writeExcel()
readExcel()