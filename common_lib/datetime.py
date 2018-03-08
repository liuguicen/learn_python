# -*- coding: utf-8 -*-
from datetime import datetime
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')
# dt = datetime(2015, 4, 19, 12, 20, 6) # 用指定日期时间创建datetime
# print(dt)
# t = datetime.timestamp(datetime.now())
# print(datetime.fromtimestamp(t)) # 本地时间
# print(datetime.utcfromtimestamp(t)) # UTC时间
print(datetime.now().strftime('%Y年%m月%d日'))
