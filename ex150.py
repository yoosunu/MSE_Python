List = ["가", "나", "다", "라"]
for i in List[: :-1]: # i가 List의 원소인 '가','나','다','라'의 값을 가지며 for문이 반복되는데, [: :-1]에서 -1(증감폭)을 넣어줌으로써 "라","다","나","가"순으로 값을 슬라이싱 하게 된다. 
    print(i)