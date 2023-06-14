def solution(a, b):
    rst = 0
    for i in range(len(a)):
        rst += a[i] * b[i]

    return rst