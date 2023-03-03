N = int(input())
plane = [[0] * 1001 for _ in range(1001)]
lst = []
for k in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            plane[i][j] = k
for K in range(1, N + 1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if plane[i][j] == K:
                cnt += 1
    print(cnt)