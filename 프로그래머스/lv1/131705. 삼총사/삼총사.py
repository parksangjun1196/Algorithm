def solution(number):

    a = number
    rst = 0
    for i in range(len(a)-2):

        for j in range(i+1,len(a)-1):

            for k in range(j+1,len(a)):
                if a[i] + a[j] + a[k] == 0:
                    rst += 1
    
    return rst