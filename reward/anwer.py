def dfs(count):
    global answer
    if not count:
        tmp = int(''.join(numbers))
        if answer < tmp:
            answer = tmp
        return
    for i in range(length):
        for j in range(i+1, length):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            tmp_key = ''.join(numbers)
            if visited.get((tmp_key, count - 1), 1):
                visited[(tmp_key, count - 1)] = 0
                dfs(count - 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())
for tc in range(1, T+1):
    numbers, change = input().split()
    numbers = list(numbers)
    change = int(change)
    length = len(numbers)
    answer = -1
    visited = {}
    dfs(change)
    print(f'#{tc} {answer}')
