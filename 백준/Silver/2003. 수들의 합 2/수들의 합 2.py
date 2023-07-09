n, m = map(int,input().rsplit())
alist = list(map(int,input().rsplit()))

l, r = 0, 0
rst, hap = 0, 0

for l in range(n):
    while hap < m and r < n:
        hap += alist[r]
        r += 1
    if hap == m:
        rst += 1
    hap -= alist[l]

print(rst)