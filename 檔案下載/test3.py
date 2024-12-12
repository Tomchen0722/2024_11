from datetime import time
some_time = time(10, 35)
fmt = "日期是 %b, %d, %y,時間是 %i:%Mm:%s%p"
some_time.strftime(fmt)

print(fmt)
'日期是 January, 01, 1900,時間是 10:35:00AM'