def solution(citations):
    
    citations = sorted(citations)
    tp = 0
    idx = 0
    # 0 1 3 5 6
    for i in range(len(citations)):
        if citations[-1] == 0:
            return 0
        # 0 1 2 3 4 
        if citations[i] >= len(citations[i:]):
            return len(citations[i:])
            
    
    
    # return 
    