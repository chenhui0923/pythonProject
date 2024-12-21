import os
import glob
import pandas as pd
import shutil


def readExcel(NCexcel):
    yue = pd.read_excel(NCexcel, sheet_name='①ebs202407科目余额表')
    kemu = pd.read_excel(NCexcel, sheet_name='②科目对应表')
    yue1 = yue[~yue['科目编号'].str.contains('HH')]#去掉HH的


    table = pd.merge(yue1,kemu,how='left',on='科目编号')


    # print(yue)
    # print("----")
    print(kemu)
    # print("----")



if __name__ == '__main__':
    # NCexcel = input("输入所需提取的NCexcel文件：")
    NCexcel = r"C:\Users\Administrator\Desktop\副本NC凭证生成数据.xlsx"
    readExcel(NCexcel);