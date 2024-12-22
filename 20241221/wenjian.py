import os
import shutil
import pdfplumber
import re


def search_dir(path):
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            search_dir(entry_path)  # 递归搜索子目录
        else:
            if not entry_path.endswith('_apply.pdf'):
                file_path1.append(entry_path);
                # print(file_path1)
    for pdf in file_path1:
        filenames = os.path.basename(pdf)
        old_file = pdf
        dst_file = os.path.join(qianyi_path,os.path.basename(filenames))
        shutil.copyfile(old_file, dst_file)

def re_text(bt, text):
    m1 = re.search(bt, text)
    if m1 is not None:
        return re_block(m1[0])

def re_block(text):
    return text.replace(' ', '').replace('　', '').replace('）', '').replace(')', '').replace('：', ':')

def get_pdf(dir_path):
    pdf_file = []
    for root, sub_dirs, file_names in os.walk(dir_path):
        for name in file_names:
            if name.endswith('.pdf'):
                filepath = os.path.join(root, name)
                pdf_file.append(filepath)
    return pdf_file


def read(qianyi_path):
    # filenames = get_pdf(r'C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试')  # 修改为自己的文件目录
    filenames = get_pdf(qianyi_path)
    for filename in filenames:
        # print(filename)
        with pdfplumber.open(filename) as pdf:
            first_page = pdf.pages[0]
            pdf_text = first_page.extract_text()
            if '发票' not in pdf_text:
                continue
            print(pdf_text)
            print('--------------------------------------------------------')
            print(re_text(re.compile(r'[\u4e00-\u9fa5]+电子普通发票.*?'), pdf_text))
            t2 = re_text(re.compile(r'[\u4e00-\u9fa5]+专用发票.*?'), pdf_text)
            if t2:
                print(t2)
            # print(re_text(re.compile(r'发票代码(.*\d+)'), pdf_text))
            item = re_text(re.compile(r'发票号码(.*\d+)'), pdf_text)
            if item is not None:
                item = re.sub(r'发票号码(:|: |：)', '', item)
                item = item.replace(' ', '')
                print(item)
            item3 = re_text(re.compile(r'名\s*称\s*[:：]\s*([\u4e00-\u9fa5]+)'), pdf_text)
            if item3 is not None:
                item3 = re.sub(r'名称(:|: |：)', '', item3)
                item3 = item3.replace(' ', '')
                print(item3)
            # print(re_text(re.compile(r'开票日期(.*)'), pdf_text))
            # print(re_text(re.compile(r'名\s*称\s*[:：]\s*([\u4e00-\u9fa5]+)'), pdf_text))
            # print(re_text(re.compile(r'纳税人识别号\s*[:：]\s*([a-zA-Z0-9]+)'), pdf_text))
            # price = re_text(re.compile(r'小写.*(.*[0-9.]+)'), pdf_text)
            #
            # company = re.findall(re.compile(r'名.*称\s*[:：]\s*([\u4e00-\u9fa5]+)'), pdf_text)
            # if company:
            #     print(re_block(company[len(company)-1]))
            # print('--------------------------------------------------------')
            name1.append(filename)
            name2.append(item)
            name3.append(item3)
            # 处理下面表格的数据
            table = first_page.extract_tables()[0]
            for t in table[1]:
                if not t:
                    continue
                t_ = str(t).replace(" ", "")  # 去掉空格

                ts = t_.split("\n")
                if "车牌号" in t_:
                    if len(ts) > 1 :
                        name4.append(ts[1])
                    else:
                        name4.append("")
                if "通行日期起" in t_:
                    if len(ts) > 1 :
                        name5.append(ts[1])
                    else:
                        name5.append("")
                # if "单位" in t_:
                #     if len(ts) > 1:
                #         all_fields["单位"].append(ts[1])
                #     else:
                #         all_fields["单位"].append("")
                # if "数量" in t_:
                #     if len(ts) > 1:
                #         all_fields["数量"].append(ts[1])
                #     else:
                #         all_fields["数量"].append("")
                # if "单价" in t_:
                #     if len(ts) > 1:
                #         all_fields["单价"].append(ts[1])
                #     else:
                #         all_fields["单价"].append("")
                # if "税率" in t_:
                #     if len(ts) > 1:
                #         all_fields["税率"].append(ts[1])
                #     else:
                #         all_fields["税率"].append("")
                # if "金额" in t_:
                #     if len(ts) > 1:
                #         all_fields["金额"].append(ts[1])
                #     else:
                #         all_fields["金额"].append("")
                # if "税额" in t_:
                #     if len(ts) > 1:
                #         all_fields["税额"].append(ts[1])
                #     else:
                #         all_fields["税额"].append("")
            # print(all_fields);




if __name__ == '__main__':
    file_path1 = []  #用来看所提取的文件名
    file2 = []  # 用于存储excel 文件中的发票号
    name1 = []
    name2 = [] #发票号
    name3 = []
    name4 = [] # 车牌号
    name5 = [] # 通行日期起
    # file_path = r"C:\Users\Administrator\Desktop\2024ETC变更后"
    # qianyi_path = r'C:\Users\Administrator\Desktop\迁移1'
    file_path = input("输入所需提取的文件夹路径：")
    qianyi_path = input("输入迁移的目标文件夹：")
    search_dir(file_path);
    read(qianyi_path);
    for item1, item2, item3 ,item4, item5 in zip(name1,name2,name3,name4,name5):

        filname = os.path.dirname(item1)+ "\\"+item4+"_" +item5+"_" +item2 +'.pdf'
        print(filname)
        os.rename(item1,filname)
    # 车牌号_通行日期_发票号;