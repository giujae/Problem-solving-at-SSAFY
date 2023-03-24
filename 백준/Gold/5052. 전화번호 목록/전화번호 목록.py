import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    number = [str(input().strip()) for _ in range(n)]
    number.sort()
    temp = True
    for i in range(len(number)-1):
        if number[i] == number[i+1][:len(number[i])]:
            temp = False
    if temp:
        print('YES')
    else:
        print('NO')