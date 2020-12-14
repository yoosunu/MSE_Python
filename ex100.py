date = ['09/05', '09/06', '09/07', '09/08', '09/09'] #value로.
close_price = [10500, 10300, 10100, 10800, 11000] # key로.
close_table = dict(zip(date, close_price)) #zip()을 활용해서 close_table이라는 dict를 생성함(date를 value로, close_price를 key로).
print(close_table)