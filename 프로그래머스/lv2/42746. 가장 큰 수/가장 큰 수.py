def solution(numbers):
    ans = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    ans = str(int(''.join(numbers)))
    return ans