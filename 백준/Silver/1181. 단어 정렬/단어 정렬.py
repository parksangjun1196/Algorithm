a = int(input())
alist = []
for i in range(a):
    b = input()
    if b not in alist:
        alist.append(b)
alist = list(set(alist))
    
alist.sort(key = lambda x : (len(x),x))

for j in alist:
    print(j)