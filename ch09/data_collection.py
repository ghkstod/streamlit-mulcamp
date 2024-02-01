import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_KEY=os.getenv("SERVICE_KEY")
print(SERVICE_KEY)





'''
df=None
for i in range(1,3):
    URL=f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+(i-1)*1000}/{i*1000}/'
    print(URL)
    req= requests.get(URL)
    content=req.json()
    result=pd.DataFrame(content['tbLnOpendataRtmsV']['row'])
    df=pd.concat([df,result])
df=df.reset_index(drop=True)
df

'''