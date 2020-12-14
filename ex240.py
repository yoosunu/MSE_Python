def 함수0(num) : # 세 번째로 설명할 부분. => 밑에서 num은 14였으므로 여기서 num은 28이 됨.
    return num * 2 

def 함수1(num) : # 두 번째로 설명할 부분. => 밑에서 num은 12였으므로 여기서 num은 14가 됨.
    return 함수0(num + 2)

def 함수2(num) :   # !!첫 번째로 설명할 부분.!! # 밑에서 num = 2 이므로 여기서 num은 12가 되고 함수 1로 올라간다.
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c) # 28 출력.