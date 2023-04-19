import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
arr = [(i - 20) // 2 for i in A]
cnt = 0
w = 0
tree = [0] * (2 * n)
for i in range(n):
    tree[n + i] = (arr[i], i)

def build():
    for i in range(n-1, 0, -1):
        if tree[i<<1][0] < tree[i<<1|1][0]:
            tree[i] = tree[i<<1]
        else:
            tree[i] = tree[i<<1|1]

def query(l, r):
    l += n
    r += n
    res = (int(1e9),-1)
    while l <= r:
        if l&1:
            res = res if res[0] < tree[l][0] else tree[l]
            l += 1
        if not r&1:
            res = res if res[0] < tree[r][0] else tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return res

def f(x):
    cnt = 0
    cnt += x // 20
    x %= 20
    cnt += x // 15
    x %= 15
    cnt += x // 10
    x %= 10
    cnt += x // 5
    return cnt

def solve(l, r, prev):
    global cnt, w
    if l == r:
        cnt += f(arr[l] - prev)
        w += arr[l] - prev
        return
    if l > r : return
    val, idx = query(l, r)
    cnt += f(val - prev)
    w += val - prev
    solve(l, idx - 1, val)
    solve(idx + 1, r, val)

build()
solve(0, n-1, 0)
print(4 * w, 4 * cnt)