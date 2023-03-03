N = int(input())
count = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        if i * j <= N:
            count += 1
for i in range(1, N + 1):
    if i ** 2 <= N:
        count += 1
print(count)