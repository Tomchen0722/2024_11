import requests #命名空間
from io import StringIO
from requests import Response #要使用Response命名空間需要從requests import進來
from csv import DictReader
from requests.exceptions import RequestException,HTTPError
#r:response (提示是使用Response的命名空間)
import streamlit as st

@st.cache_data #註冊一個Function
def get_youbikes()->list[dict]:
    url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000"

    try:
        r:Response = requests.request('GET',url)
        r.raise_for_status()

    except HTTPError as e :
        raise Exception("伺服器有問題")
    except RequestException as e:
        raise Exception("連線有問題")
    else:
        print("下載成功")
        file = StringIO(r.text)
        reader = DictReader(file)
        list_reader:list[dict] = list(reader)
        return list_reader