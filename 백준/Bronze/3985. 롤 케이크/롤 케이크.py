L = int(input())
N = int(input())
cake = [0] * (L + 1)
lst2 = []
for j in range(1, N + 1):
    P, K = map(int, input().split())
    for k in range(P, K+1):
        if cake[k] == 0:
            cake[k] = j
    lst2.append([j, K-P])
lst = []
for j in range(1, N + 1):
    cnt = 0
    for i in range(1, L + 1):
        if cake[i] == j:
            cnt += 1
    lst.append([j, cnt])
mx = 0
mx2 = 0
idx = 0
idx2 = 0
for i in lst:
    if i[1] > mx:
        mx = i[1]
        idx = i[0]
for i in lst2:
    if i[1] > mx2:
        mx2 = i[1]
        idx2 = i[0]
print(idx2)
print(idx)