T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result_cross = []
    result_x = []
    for i in range(N):
        for j in range(N):
            lst_cross = []
            for k in range(-(M-1), M):
                if i+k in range(N):
                    lst_cross.append(arr[i+k][j])
                if j+k in range(N):
                    lst_cross.append(arr[i][j+k])
            lst_cross.remove(arr[i][j])
            result_cross.append(lst_cross)
            lst_x = []
            di = list(range(-(M-1), M))
            dj = list(range(-(M-1), M))[::-1]
            for k in range(len(di)):
                if i+di[k] in range(N) and j+di[k] in range(N):
                    lst_x.append(arr[i+di[k]][j+di[k]])
                if i+di[k] in range(N) and j+dj[k] in range(N):
                    lst_x.append(arr[i+di[k]][j+dj[k]])
            lst_x.remove(arr[i][j])
            result_x.append(lst_x)
    mx = 0
    mx2 = 0
    for i in result_cross:
        if mx < sum(i):
            mx = sum(i)
    for i in result_x:
        if mx2 < sum(i):
            mx2 = sum(i)
    print(f'#{tc} {max(mx, mx2)}')