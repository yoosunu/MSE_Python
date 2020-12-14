ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0 #총 수입 0
for row in ohlc[1:]: # 변수 row가 리스트 ohlc안에서 반복.
    profit += (row[3] - row[0]) # 수입은 profit + (row[3] - row[0])