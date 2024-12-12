from datetime import date
now = date.today() #取得現在時間
print(now)

#使用timedelta取得一個指定的日期
from datetime import date
from datetime import timedelta
now = date.today()
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
now + 17*one_day
print(now)
yesterday = now - one_day
print(f"昨天{yesterday}")
#使用datetime.now()取得現在日期和時間
from datetime import datetime
now = datetime.now()
now
#datetime.datetime(2021, 3, 1, 15, 27, 25, 43479)
now.month
now.day
now.hour
now.minute
now.second
now.microsecond
#使用combine()整合date和time成為datetime
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day,noon)
print(noon_today)
#從datetime取出日期和時間
from datetime import datetime
now = datetime.now()
now.date()
now.time()
#使用ctime()轉換timestamp成為字串

time.ctime(now)
#使用localtime(),gmtime()建立struct_time物件
time.localtime(now)
time.struct_time(tm_year=2021, tm_mon=3, tm_mday=1, tm_hour=19, tm_min=32, tm_sec=40, tm_wday=0, tm_yday=60, tm_isdst=0)
#建立UTCtime
time.gmtime(now)
time.struct_time(tm_year=2021, tm_mon=3, tm_mday=1, tm_hour=11, tm_min=32, tm_sec=40, tm_wday=0, tm_yday=60, tm_isdst=0)
#注意:儲存時間請使用UTC time,儲存字串請使用UTF-8
#使用strftime()將struct_time物件轉成字串
import time
fmt = "現在日期是 %A, %B %d, %Y,時間是 %I:%M:%S%p"
t = time.localtime()
time.struct_time(tm_year=2021, tm_mon=3, tm_mday=1, tm_hour=20, tm_min=6, tm_sec=38, tm_wday=0, tm_yday=60, tm_isdst=0)
time.strftime(fmt,t)
#date物件只轉換date部份
from datetime import date
some_day = date(2018, 7, 4)
fmt = "日期是 %B, %d, %Y,時間是 %I:%M:%S%p"
some_day.strftime(fmt)
#time物件只轉換time部份
from datetime import time
some_time = time(10, 35)
fmt = "日期是 %B, %d, %Y,時間是 %I:%M:%S%p"
some_time.strftime(fmt)
#使用strptime()將字串轉為date或time物件
#注意字串格式
import time
fmt = "%Y-%m-%d"
time.strptime("2012-01-29", fmt)
time.struct_time(tm_year=2012, tm_mon=1, tm_mday=29, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=29, tm_isdst=-1)
#使用local module
import locale
from datetime import date
halloween = date(2018, 10, 20)
for lang_country in  ['en_us','fr_fr','de_de','es_es','is_is','zh_tw']:
       locale.setlocale(locale.LC_TIME, lang_country)
       print(halloween.strftime('%A, %B, %d'))
