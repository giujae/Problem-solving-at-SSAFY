# 대각선 방향
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
  
def dfs(i, j, direction, cnt):  # 시작 위치, 방향 타입, 디저트 수를 매개변수로
    global result
    # 꺾기 
    if direction < 3:  # 사각형은 3번만 꺾으면 만들어짐.
        end = direction + 2
    # 직진
    else:
        end = direction + 1
    for k in range(direction, end):
        ci = i + di[k]
        cj = j + dj[k]
        if si == ci and sj == cj:  # 왔던 곳으로 돌아온다
            result = max(result, cnt)
            return
        if 0 <= ci < N and 0 <= cj < N:    # 범위 벗어나지 않는 다면
            if not visited[arr[ci][cj]]:  # 방문하지 않은 카페 
                visited[arr[ci][cj]] = 1  # 방문 처리
                dfs(ci, cj, k, cnt + 1)
                visited[arr[ci][cj]] = 0  # 리셋
  
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    visited = [0] * 101
    result = -1
    # 사각형 모양을 그리며 출발하고 카페로 돌아와야 함.
    for i in range(N):
        for j in range(N):
            si, sj = i, j
            visited[arr[i][j]] = 1
            dfs(i, j, 0, 1)
            visited[arr[i][j]] = 0
  
    print(f'#{tc} {result}')