a = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in a:
    split = i.split(".") # i가 'intra.h', 'intra.c', 'define.h', 'run.py'순으로 반복된다. 
    if (split[1] == "h") or (split[1] == "c"): #split[1]가 h거나, c면 i를 출력한다.
        print(i)