def solution(t, p):
    tglen = len(p)
    tg = int(p)
    rst = 0
    
    for i in range(len(t)-tglen+1):
        tdd = int(''.join(t[i:i+tglen]))
        if int(tdd) <= tg:
            rst += 1

    return rst