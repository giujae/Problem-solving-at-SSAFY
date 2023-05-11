import sys, heapq

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    empty = [False] * (n + 1)
    can = True
    cache = [[] for _ in range(n + 1)]
    time = [-1] * m
    for i in range(m - 1, -1, -1):
        if arr[i]:
            time[i] = arr[i]
            cache[arr[i]].append(i)

    q = []
    for i in range(1, n + 1):
        if cache[i]:
            heapq.heappush(q, cache[i].pop())
            
    ans = []
    for i in range(m):
        if arr[i]:
            if not empty[arr[i]]:
                can = False
                break
            empty[arr[i]] = False
            if cache[arr[i]]:
                heapq.heappush(q, cache[arr[i]].pop())
                
        else:
            if q:
                now = q[0]
                heapq.heappop(q)
                ans.append(time[now])
                empty[time[now]] = True
            else:
                ans.append(0)
                
    if not can:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, ans)))