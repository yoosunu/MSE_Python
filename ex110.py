if True : # if문에 True를 넣었으므로 else가 아닌 if가 작동함.
    if False:  # 위에서 if 문에 True를 넣었으므로 False를 넣은 이 if문은 작동하지 않는다.
        print("1") #출력되지 않음.
        print("2") #출력되지 않음.
    else:   # if에 False를 넣었으므로 이 else는 작동함.
        print("3") # 3출력.
else : # 작동 안함.
    print("4") #else문이 작동하지 않으므로 출력되지 않음.
print("5") # if문, else문과 관련없이 5를 출력할 것임. 