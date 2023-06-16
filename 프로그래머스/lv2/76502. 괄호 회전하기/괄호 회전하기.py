def chk(k):
    m = k + []
    dead = ["]","}",")"]
    arr = []

    for i in range(len(m)):
        
       

        if len(arr) > 0:
            
            if arr[-1] == "(" and m[0] == ")":
                arr.pop()
                m.pop(0)
                
                
            elif arr[-1] == "{" and m[0] == "}":
                arr.pop()
                m.pop(0)
              
                
            elif arr[-1] == "[" and m[0] == "]":
                arr.pop()
                m.pop(0)
            else:
                arr.append(m.pop(0))
                
        else:
            arr.append(m.pop(0))
                
     
       
        
    if len(arr) == 0 and len(m) == 0:
   
        return True
    else:
     
        return False
                
    
    
def solution(s):
    
    d = list(s)
    cnt = 0
    for i in range(len(s)):
        
        if chk(d) == True:
            cnt += 1

        d.append(d.pop(0))

    return cnt
solution("[](){}")
