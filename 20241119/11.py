import pdfplumber
import re
import os

#  pyinstaller --onefile --strip 11.py 打包方式

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

def read(file_path):
    # filenames = get_pdf(r'C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\测试')  # 修改为自己的文件目录
    filenames = get_pdf(file_path)
    for filename in filenames:
        # print(filename)
        with pdfplumber.open(filename) as pdf:
            first_page = pdf.pages[0]
            pdf_text = first_page.extract_text()
            if '发票' not in pdf_text:
                continue
            # print(pdf_text)
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
                # print(item)
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

if __name__ == '__main__':
    file_path = input("输入所需提取的文件夹路径：")
    name1 = []
    name2 = []
    name3 = []
    read(file_path)
    for item1, item2, item3 in zip(name1,name2,name3):

        filname = os.path.dirname(item1)+ "\\"+"dzfp_"+item2+"_" +item3 +'.pdf'

        os.rename(item1,filname)
        # print(filname,item2)