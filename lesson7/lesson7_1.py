import requests #命名空間
from io import StringIO
from requests import Response #要使用Response命名空間需要從requests import進來
from csv import DictReader
#r:response (提示是使用Response的命名空間)
url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000"

r:Response = requests.request('GET',url)
if r.status_code == 200:
    print("下載成功")
    file = StringIO(r.text)
    reader = DictReader(file)
    list_reader:list[dict] = list(reader)
    print(list_reader)
else:
    print("下載失敗")
