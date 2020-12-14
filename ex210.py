def message1(): # 함수 정의 => A를 출력하라.
    print("A")

def message2(): # 함수 정의 => B를 출력하라.
    print("B")

def message3(): # 함수 정의 => message2, c 순으로 3번 반복해서 출력함.
    for i in range (3) :
        message2()
        print("C")
    message1() # message1 출력.

message3() # BCBCBCA출력.