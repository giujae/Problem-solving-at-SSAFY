dx = [1, 0]
dy = [0, 1]
 
def move(x, y, total):
    global answer
 
    if answer < total:
        return
 
    if x == y == n - 1:
        if total < answer:
            answer = total
        return
 
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= n - 1 and ny <= n - 1:
            move(nx, ny, total + arr[ny][nx])
 
 
tc = int(input())
for idx in range(1, tc + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += arr[i][j]
    move(0, 0, arr[0][0])
    print(f'#{idx} {answer}')