from collections import deque
## input 
n, m, v = map(int,input().split())

## 
tglist = [[]*i for i in range(n+1)]

bangmun = [0] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    tglist[a].append(b)
    tglist[b].append(a)
    
for t in range(n+1):
    tglist[t].sort()

def dfs(v):
    print(v, end=" ")
    for i in tglist[v]:
        if bangmun[i] == 0:
            bangmun[i] = 1
            dfs(i)
    
bangmun[v] = 1 


def bfs(v):
    bangmun = [0] * (n+1)
    q = deque()
    q.append(v)       
    bangmun[v] = 1   
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in tglist[v]:
            if bangmun[i] == 0:
                q.append(i)
                bangmun[i] = 1

    
    
## [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
## [0,1,0,0,0]   
    
    
dfs(v)
print()
bfs(v)
    
    
    


