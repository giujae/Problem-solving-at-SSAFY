T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bread = [0]*11112
    cnt = 0
    arr.sort()
    for i in range(M, 11112, M):
        cnt += K
        for j in range(M):
            if i+j < 11112:
                bread[i+j] = cnt
    for k in arr:
        for i in range(k, 11112):
            bread[i] -= 1
    for i in bread:
        if i < 0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')