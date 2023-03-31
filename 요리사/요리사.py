def total(food):
    sm = 0
    for i in food:
        for j in food:
            if i != j:
                sm += arr[i][j]
    return sm

def dfs(n):
    global mn
    c = [1, 0]
    if sum(check) == N//2:
        A = []
        B = []
        for k in range(len(check)):
            if check[k]:
                A.append(k)
            else:
                B.append(k)
        A_total = total(A)
        B_total = total(B)
        if abs(A_total - B_total) < mn:
            mn = abs(A_total - B_total)
    elif n == N:
        return
    else:
        for i in range(2):
            check[n] = c[i]
            if check[0]:
                dfs(n+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    mn = 20000 * 2
    dfs(0)
    print(f'#{tc} {mn}')