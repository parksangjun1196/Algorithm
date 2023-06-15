def solution(progresses, speeds):
    rst = []
    while len(progresses) != 0:
        cnt = 0
     
        while progresses[0] >=100:
            if len(progresses) <= 0:
                rst.append(1)
                return rst
      
            progresses.pop(0)
            speeds.pop(0)
            cnt +=1
            if len(progresses) <= 0:
                rst.append(cnt)
                return rst
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        if (cnt != 0):
            rst.append(cnt)
    return rst