import requests
from lxml import etree
from urllib.request import urlretrieve
from my_fake_useragent import UserAgent
import os

# https://blog.csdn.net/z55947810/article/details/105583431
# 百度反扒
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Host': 'tieba.baidu.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'User-Agent': UserAgent().random(),
    'Referer': 'https://tieba.baidu.com/f?ie=utf-8&kw=%E8%A1%A8%E6%83%85%E5%90%A7&p_tk=5580VzrIEgkV5%2BfzEgwsLlj8G9InbYy6Dnvtn0RQHHAas6G9eLx%2BCde6jnTMRw1OUvkO2ZsDYhj6b%2BRK9CWHobI0V3ArvoHyixd1W%2FyONkwWG4S%2FSb0znqel3%2FERKiuiMb7sIHmfbKJMpXjeZ6sA15zvqbq5qhLJnF4VPDCJwM8T7hM%3D&p_timestamp=1692322080&p_sign=9d0d1cb32ad33c72123d8d95f6b8e058&p_signature=e08b1e1f2aea39075f284bb997565d16&__pc2ps_ab=5580VzrIEgkV5%2BfzEgwsLlj8G9InbYy6Dnvtn0RQHHAas6G9eLx%2BCde6jnTMRw1OUvkO2ZsDYhj6b%2BRK9CWHobI0V3ArvoHyixd1W%2FyONkwWG4S%2FSb0znqel3%2FERKiuiMb7sIHmfbKJMpXjeZ6sA15zvqbq5qhLJnF4VPDCJwM8T7hM%3D|1692322080|e08b1e1f2aea39075f284bb997565d16|9d0d1cb32ad33c72123d8d95f6b8e058',
    'Cookie': 'PSTM=1660009411; BIDUPSID=651FABC80474AF93A76D9C3E08CB2F34; BAIDUID=D3663BF56246C07635266938ACFA6824:SL=0:NR=10:FG=1; BD_UPN=12314753; BDUSS=Eo5SnY3bmhjaFF3cWNweGhWQ1RycGxuMnByd1NEZ0t2b0VKWkVyMmJEdmE5MFJrSVFBQUFBJCQAAAAAAAAAAAEAAADoRPdm09q56bO~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANpqHWTaah1kO; BDUSS_BFESS=Eo5SnY3bmhjaFF3cWNweGhWQ1RycGxuMnByd1NEZ0t2b0VKWkVyMmJEdmE5MFJrSVFBQUFBJCQAAAAAAAAAAAEAAADoRPdm09q56bO~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANpqHWTaah1kO; MCITY=-300%3A; H_WISE_SIDS=132550_216839_213361_214803_110085_243876_244722_254835_257289_257737_257015_253022_259312_261722_236312_261868_256419_263897_256222_265319_265615_265853_265881_265989_265312_261036_265277_266324_266354_266758_265887_265776_267302_267372_267375_266844_267452_267406_265986_256154_266188_267899_260335_259080_264354_266714_265368_107320_268567_268592_263618_268031_268856_269088_234295_234208_267537_259642_269389_264170_267780_269549_269665_203518_269731_269772_269775_269831_268445_267344_269905_262559_270182_270084_269034_264812_267066_269160_256739_270204_270460_267530_270663_270482_270548_270922_267659_270321_270968_271035_271019_257179_268876_271099_236536_271170_271175_271078_270101; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_ODc3MjZiOGZhZjZhNzhhMjkzOTlmNTYzYWY4YThkNmEyYzVjMWM2YjBmMDY3ZDIzMTI5MjJkNjlkOTE3MzNiODI0OTllZTAwMDc5NzY0ZTk1OTVhMjMyMTExYzBmMzAxZGZiMzVlZmJlYWNlMjMxNDc3YjA4ZDQ1NTdiNWVmNzI5M2I4ZjMxMDc5NWE4MGRkZjFjODEwMjgxOTNhYTY0OA==; ai-studio-ticket=1F4F22C447CE459688A73DD227EB8F4A573176F0B88B46BDB06F0BA89E78B695; sug=3; sugstore=0; ORIGIN=2; bdime=0; BAIDUID_BFESS=D3663BF56246C07635266938ACFA6824:SL=0:NR=10:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=3; COOKIE_SESSION=1062_0_8_8_6_9_1_0_7_6_1_0_12415_0_0_0_1691745123_0_1691746180%7C9%2390008_17_1691461432%7C9; H_PS_PSSID=36552_39113_39008_39114_39040_38918_26350_39138_39139_39137_39100_38952; H_PS_645EC=e7f55B9VH72xEblVqj2l3lMldL63kQPIv4tgFJjmmeuXBtdPMTaZ9HAdDnw7BnHuPyRD; BA_HECTOR=ag20aka1a02g002g0h048la61idbvvb1p; ZFY=qEtOt3Vdr3DzQCrM7jbryNoZrv2rAncwr3CxbMUJXoU:C; BDSVRTM=0',
}


def get_one_page(url):
    base = 'https://tieba.baidu.com'
    response = requests.get(url, headers).text
    html = etree.HTML(response)
    link_list = html.xpath('//a[@class="j_th_tit "]/@href')
    print(response)
    link_list = map(lambda link: base + link, link_list)
    # return link_list
    for link in link_list:
        print(link)


def parse_one_page(link):
    imgs = []
    url = link
    response = requests.get(url, headers).text
    html = etree.HTML(response)
    img = html.xpath('//img[@class="BDE_Image"]//@src')
    imgs.append(img)
    return imgs


def main():
    url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E8%A1%A8%E6%83%85%E5%90%A7'
    get_one_page(url)


def binp():
    index_url = "https://tieba.baidu.com/p/5475267611"
    r = requests.get(index_url).text
    print(r)
    selector = etree.HTML(r)
    imgURL = selector.xpath('//img[@class="BDE_Image"]/@src')
    for imgURL in imgURL:
        print(imgURL)


if __name__ == '__main__':
    # geturl()
    # getdoubanurl()
    # binp()
    main()
