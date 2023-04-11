def recursion(s, l, r):
    global cnt
    global answer
    cnt += 1
    if l >= r:
        answer = 1
        return
    elif s[l] != s[r]:
        answer = 0
        return
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    answer = 0
    s = input()
    isPalindrome(s)
    print(f'{answer} {cnt}')