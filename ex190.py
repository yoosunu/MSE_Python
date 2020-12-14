apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart: # 변수 row가 리스트 apart의 값을 가지며 반복.
    for col in row:  # for문 안에 for문, 변수 col가 row값이 반복됨에 따라서 col도 반복함.
        print(col, "호") #col 뒤에 '호' 출력.
print("-" * 5)