
def solution(priorities, location):
    
    vt = [i for i in range(len(priorities))]
    tg = vt[location]
    st = []
    std = []

    cnt = 0
    while len(priorities) > 0:
        
        if priorities[0] != max(priorities):
            
            priorities.append(priorities.pop(0))
            vt.append(vt.pop(0))
            cnt += 1
            
        if priorities[0] == max(priorities):
            st.append(priorities.pop(0))
            std.append(vt.pop(0))

    return std.index(tg) + 1