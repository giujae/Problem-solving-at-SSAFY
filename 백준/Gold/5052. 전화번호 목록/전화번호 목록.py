import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    call = [str(input().strip()) for _ in range(n)] # 전화번호를 문자열로 받는다.
    call.sort() # 오름차순으로 정렬하여 사전순으로 정렬
    chek = "yes" # 일관성이 있는지 체크

    # 반복문을 통해 전화번호를 확인
    for i in range(len(call) - 1):

        # 현재 전화번호의 문자열과 다음 전화번호의 현재 전화번호 길이만큼의 문자열과 같은지 확인
        # 같으면 일관성이 없는 것
        if call[i] == call[i + 1][0:len(call[i])]:
            chek = "no"

    if chek == "no":
        print("NO")
    else:
        print("YES")