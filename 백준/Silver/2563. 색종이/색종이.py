N = int(input())
cnt = 0
paper = [[0]*100 for _ in range(100)]
for _ in range(N):
    l, r = map(int, input().split())
    for i in range(l, l+10):
        for j in range(r, r+10):
            paper[i][j] = 1
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)