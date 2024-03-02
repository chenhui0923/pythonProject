import xlwings as xw

# https://blog.csdn.net/xcntime/article/details/131628598
# https://blog.csdn.net/u010719791/article/details/120047153

# pip install xlwings


app = xw.App(visible=True, add_book=False)
app.display_alerts =False     # 关闭一些提示信息，可以加快运行速度。 默认为 True。
app.screen_updating = True    # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。
# wb = app.books.add()    #  新建一个工作表
wb = app.books.open(r\'website')
sht = wb.sheets.active