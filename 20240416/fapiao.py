import re

import pdfplumber

def extract_invoice_number(pdf_path):
    # 打开PDF文件
    with pdfplumber.open(pdf_path) as pdf:
        # 遍历PDF的每一页
        for page in pdf.pages:
            # 提取当前页的文本
            text = page.extract_text()
            invoice = {}
            # print(text)
            if text:
                # 在文本中搜索发票号码的模式
                # 假设发票号码是固定的格式，例如：011002301711
                # 这里使用了简单的字符串查找，你可能需要根据实际PDF内容调整
                item = re.search(r'发票号码(:|: |: )(\d+)',text)
                print(item)
                if item is not None:
                    item = item.group()
                    item = re.sub(r'发票号码(:|: |：)', '', item)
                    item = item.replace(' ', '')
                    return item


# 替换为你的PDF文件路径
file_path = input("输入所需提取的文件夹路径：")
pdf_path = r'C:\Users\Administrator.DESKTOP-JLQ33MI\Desktop\冯琳-16962915-继续教育.pdf'
invoice_number = extract_invoice_number(pdf_path)
print(f"提取到的发票号码是：{invoice_number}")