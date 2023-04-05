import heapq
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    rep = [i for i in range(N)]
    queue = []
    for i in range(N-1):
        for j in range(i+1, N):
            heapq.heappush(queue, (abs(x[i] - x[j])**2 + abs(y[i] - y[j])**2, i, j))
    answer = 0
    cnt = 0
    while queue:
        dist, a, b = heapq.heappop(queue)
        if find_set(a) != find_set(b):
            union(a, b)
            answer += E * dist
            cnt += 1
        if cnt == N-1:
            break
    print(f'#{tc} {round(answer)}')