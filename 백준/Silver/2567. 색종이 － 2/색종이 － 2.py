N = int(input())
perimeter = 0
paper = [[0]*101 for _ in range(101)]
for _ in range(N):
    l, r = map(int, input().split())
    for i in range(l, l+10):
        for j in range(r, r + 10):
            paper[i][j] = 1
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            for k in range(4):
                si = i + di[k]
                sj = j + dj[k]
                if paper[si][sj] == 0:
                    perimeter += 1
print(perimeter)