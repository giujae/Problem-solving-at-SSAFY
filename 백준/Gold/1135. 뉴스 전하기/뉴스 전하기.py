n = int(input())
t = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for idx in range(1, n):
    tree[t[idx]].append(idx)
time = [False]*n
def dp(v):
    child_t = []
    for i in tree[v]:
        dp(i)
        child_t.append(time[i])
    if not tree[v]:
        child_t.append(0)

    child_t.sort(reverse=True)
    need_time = [child_t[i]+i+1 for i in range(len(child_t))]
    time[v] = max(need_time)
    
dp(0)
print(time[0]-1)