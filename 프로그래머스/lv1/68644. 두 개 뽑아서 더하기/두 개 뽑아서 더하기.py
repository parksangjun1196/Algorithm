def solution(numbers):
    st = []
    
    for i in range(len(numbers)):
        
        for j in range(i+1,len(numbers)):
   
            st.append(numbers[i] + numbers[j])
    
    st = sorted(list(set(st)))

    return st