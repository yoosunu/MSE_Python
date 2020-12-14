low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = [] # 리스트 지정.
for i in range(len(low_prices)) : # 5번 반복.
    volatility.append(high_prices[i] - low_prices[i]) # 변동폭을 리시트에 저장.