def solution(phone_number):
    answer = ''
    a = phone_number[-4:]
    b = len(phone_number) - 4
    c = "*" * b
    answer = c + str(a)
    return answer