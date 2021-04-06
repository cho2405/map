import requests
import json
import pandas as pd

url = 'https://m.land.naver.com/cluster/ajax/articleList?rletTpCd=TJ&tradTpCd=A1&z=14&lat=37.5171001&lon=127.3344533&btm=37.4868331&lft=127.2879331&top=37.5473548&rgt=127.3809735&showR0=&totCnt=116&cortarNo='

body = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36',
}
r = requests.get(url,headers=body)
data = json.loads(r.text)
tj_df = pd.json_normalize(data['body'])
tj_df.columns
