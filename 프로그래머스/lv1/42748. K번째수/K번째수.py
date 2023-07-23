def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        narray = array[commands[i][0]-1:commands[i][1]]
        narray.sort()

        answer.append(narray[commands[i][2]-1])
    return answer

