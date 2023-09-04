def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    b = denom1 * denom2
    a = numer2*denom1 + numer1*denom2
    c = (gcd(a,b))
    return [a//c, b//c]