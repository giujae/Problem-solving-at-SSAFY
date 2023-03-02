N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
lst = []
for i in A:
    if i - B > 0:
        if (i - B) % C == 0:
            lst.append((i - B) // C)
        else:
            lst.append((i - B) // C + 1)
if len(lst) != 0:
    print(sum(lst) + len(A))
else:
    print(1)