import math

def solution(price):

    if price >= 500000:
        price = math.trunc(price*0.8)
    elif 500000>price>=300000:
        price = math.trunc(price*0.9)
    elif 300000>price>=100000:
        price = math.trunc(price*0.95)
        
    print(math.trunc(price))
    return price