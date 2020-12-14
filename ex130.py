import requests   
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price']) # 변동폭을 최고가 - 최저가로 정의.
시가 = float(btc['opening_price']) # 시가 정의.
최고가 = float(btc['max_price']) # 최고가 정의.

if (시가+변동폭) > 최고가:  # 시가+변동폭이 최고가보다 높을 경우 "상승장" 출력.
    print("상승장")
else:  # 그렇지 않을 경우 "하락장" 출력.
    print("하락장")
