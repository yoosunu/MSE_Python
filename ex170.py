result = 1 # 이전 값을 계속 곱해주기 위함(초기 값 = 1).
for i in range(1, 11, 1) :
    result *= i  # i가 2일 때 => 2 * 1 = 2, i가 3일 때 => 3 * 2 = 6 즉 이전 값이 i가 반복 되어 바뀔 때마다 곱해짐.
print(result)