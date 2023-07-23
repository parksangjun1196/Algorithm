def solution(nums):
 
    lend = len(nums)//2
    newnums = list(set(nums))

    if lend < len(newnums):
    
        return lend
    else:

        return len(newnums)
    return answer