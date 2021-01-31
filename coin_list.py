import json
import requests
import pandas as pd

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'

resp = requests.get(url)
data = json.loads(resp.content)
df = pd.DataFrame(data)

selected = df[['name','symbol','market_cap']]
print(selected.head(30))

