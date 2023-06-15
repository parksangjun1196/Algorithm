def solution(n):
    
    cnt = 0
    for i in range(1,n+1):
        rt = 0
        for j in range(i,n+1):
            rt += j
            
            if rt == n:
                cnt += 1
            if rt > n:
                break
            

    return cnt