from datetime import datetime
import  time


# 五位数时间戳转换
def date(sa):
    delta = (sa - 70 * 365 - 19) * 86400 - 8 * 3600
    print(delta)
    timeArray = time.localtime(delta)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    print(otherStyleTime)
    return otherStyleTime




date(45407)