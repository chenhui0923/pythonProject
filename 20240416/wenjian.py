import os
import glob
import pandas as pd
import shutil



def main(file_path,file2):
    if not os.path.isdir(file_path):
        raise ValueError(f"{file_path} is not a directory.") #判断是文件夹

    pdf_files = glob.glob(os.path.join(file_path, "*.pdf"))
    filenames = [os.path.basename(pdf) for pdf in pdf_files]
    for files in filenames:
        sptext = files.split("_")[1]
        # print(sptext,file2)
        if sptext in file2[0]:
            old_file = file_path + "/" + files
            dst_file = os.path.join(qianyi_path,os.path.basename(files))
            # print(old_file,dst_file)
            shutil.copyfile(old_file,dst_file)


def excel(excel_path):
    df = pd.read_excel(excel_path)
    column_data = df['发票号'].values.tolist()
    # print(column_data)
    file2.append(column_data)


# def arry():
#     first = []
#     for sub in file1:
#         first.append(sub[0])
#     inters = np.intersect1d(first,file2)
#     print(inters,file1)
#     matchs = find

if __name__ == '__main__':
    file1 = []  #用来看所提取的文件名
    file2 = []  #用于存储excel 文件中的发票号
    # file3 = []  #上面两个数据的交集

    # file_path = r"C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试数据\202403"
    # file_path = r"C:/Users/Administrator/Desktop/测试数据/202403"

    # excel_path = r"C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试数据\票号.xlsx"
    # excel_path = r"C:/Users/Administrator/Desktop/测试数据/票号.xlsx"
    # qianyi_path = r'C:/Users/Administrator/Desktop/迁移文件夹'
    file_path = input("输入所需提取的文件夹路径：")
    excel_path = input("输入所需提取的excel文件")
    qianyi_path = input("输入迁移的目标文件夹")
    excel(excel_path)

    main(file_path,file2)

    # arry()
    print(file1)

