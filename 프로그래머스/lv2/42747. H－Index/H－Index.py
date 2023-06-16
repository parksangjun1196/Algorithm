def solution(citations):
    
    citations = sorted(citations)
    for i in range(len(citations)):
        print(len(citations)-i-1)
        
        if citations[len(citations)-i-1] <= len(citations[len(citations)-i-1:]):
            print(citations[len(citations)-i-1])
            tg = citations[len(citations)-i-1]
            while True:
                
                if tg > len(citations[len(citations)-i-1:]):
                    
                    return tg-2
                tg += 1
                
            
            return citations[len(citations)-i-1]
