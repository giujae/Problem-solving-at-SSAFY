import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
char = list(map(str, sys.stdin.readline().split()))
answer = []
lst = []
possible = list(combinations(char, L))
for i in possible:
    answer.append(''.join(sorted(i)))
for i in answer:
    vow = 0
    for j in i:
        if j in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
    if L-vow >= 2 and vow >= 1:
        lst.append(i)
lst.sort()
for i in lst:
    print(i)