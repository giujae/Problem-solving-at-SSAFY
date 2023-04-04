import heapq
def find(fuel, start):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dist = [[int(1e9)] * N for _ in range(N)]
    dist[start][start] = 0
    queue = [(0, start)]
    while queue:
        x, y = heapq.heappop(queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny <N:
                height_diff = 0
                if fuel[nx][ny] > fuel[x][y]:
                    height_diff = fuel[nx][ny] - fuel[x][y]
                if dist[nx][ny] > dist[x][y] + height_diff + 1:
                    dist[nx][ny] = dist[x][y] + height_diff +1
                    heapq.heappush(queue, (nx, ny))
    return dist

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    fuel = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {find(fuel, 0)[N-1][N-1]}')