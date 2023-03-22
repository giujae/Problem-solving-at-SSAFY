from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 9999
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i,j])
for i in combinations(chicken, M):
    temp = 0
    for j in house:
        chicken_dist = N**2
        for k in range(M):
            chicken_dist = min(chicken_dist, abs(j[0]-i[k][0]) + abs(j[1]-i[k][1]))
        temp += chicken_dist
    result = min(result, temp)
print(result)