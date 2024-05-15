import os
import glob
import pandas as pd
import shutil



def excel(excel_path):
    df = pd.read_excel(excel_path)
    column_data = df['发票号'].values.tolist()
    # print(column_data)
    file2.append(column_data)

def search_dir(path):
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            search_dir(entry_path)  # 递归搜索子目录
        else:
            if entry_path.endswith('.pdf'):
                file_path1.append(entry_path);
    for pdf in file_path1:
        filenames = os.path.basename(pdf)
        # print(filenames,pdf)
        sptext = filenames.split("_")[1]
        if sptext in file2[0]:
            old_file = pdf
            dst_file = os.path.join(qianyi_path,os.path.basename(filenames))
            shutil.copyfile(old_file, dst_file)

def EXCELPATH():
    testqw=[]
    nerong = []
    for pdf in file_path1:
        filenames = os.path.basename(pdf)
        sptext = filenames.split("_")[1]
        testqw.append(sptext)

    for sptext1 in file2[0]:
        if sptext1 not in testqw:
            nerong.append(sptext1)
    print(nerong)
    info_website = pd.DataFrame({'缺失发票数据': nerong})
    writer = pd.ExcelWriter('缺失发票数据.xlsx')
    info_website.to_excel(writer)
    writer.close()
    print('输出成功')
if __name__ == '__main__':
    file_path1 = []  #用来看所提取的文件名
    file2 = []  #用于存储excel 文件中的发票号
    file3 = []  #处理不存在的发票号

    # file_path = r"C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试数据"
    # file_path = r"C:\Users\Administrator\Desktop\测试数据"

    # excel_path = r"C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试数据\票号.xlsx"
    # excel_path = r"C:\Users\Administrator\Desktop\测试数据\票号.xlsx"
    # qianyi_path = r'C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\迁移文件夹'
    # qianyi_path = r'C:\Users\Administrator\Desktop\迁移'

    #
    file_path = input("输入所需提取的文件夹路径：")
    excel_path = input("输入所需提取的excel文件：")
    qianyi_path = input("输入迁移的目标文件夹：")

    excel(excel_path)
    search_dir(file_path);
    EXCELPATH();
