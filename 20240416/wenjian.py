import os
import glob
import pandas as pd
import shutil



def main(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(path + "\\" + file):
            search_dir(path + "\\" + file)
        else:
            if file.endswith('.pdf'):
                file_path1.append(file)

    print(file_path1)
    filenames = [os.path.basename(pdf) for pdf in file_path1]
    for files in filenames:
        sptext = files.split("_")[1]
        # print(sptext,file2)
        if sptext in file2[0]:
            old_file = file_path + "/" + files
            dst_file = os.path.join(qianyi_path,os.path.basename(files))
            print(old_file,dst_file)
            # shutil.copyfile(old_file,dst_file)


def excel(excel_path):
    df = pd.read_excel(excel_path)
    column_data = df['发票号'].values.tolist()
    # print(column_data)
    file2.append(column_data)

def search_dir(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(path+"\\"+file):
            search_dir(path + "\\" + file)
        else:
            if file.endswith('.pdf'):
                file_path1.append(path + "\\" + file)

    print(file_path1)


if __name__ == '__main__':
    file_path1 = []  #用来看所提取的文件名
    file2 = []  #用于存储excel 文件中的发票号
    # file3 = []  #上面两个数据的交集

    file_path = r"C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试数据"
    # file_path = r"C:/Users/Administrator/Desktop/测试数据/202403"

    excel_path = r"C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试数据\票号.xlsx"
    # excel_path = r"C:/Users/Administrator/Desktop/测试数据/票号.xlsx"
    qianyi_path = r'C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\迁移文件夹'

    #
    # file_path = input("输入所需提取的文件夹路径：")
    # excel_path = input("输入所需提取的excel文件：")
    # qianyi_path = input("输入迁移的目标文件夹：")

    excel(excel_path)
    search_dir(file_path);
    # main(file_path)
