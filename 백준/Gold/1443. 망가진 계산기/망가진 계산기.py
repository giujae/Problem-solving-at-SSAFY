# 코드
# 현재 값 자리수 계산
def length(value):
    cnt = 0
    while value > 0:
        cnt += 1
        value //= 10

    return cnt

# 최대값 계산
def max_value(d, cnt, value):
    # 앞서 나온 결과이거나 d 자리수를 넘어서는 경우 종료
    if (cnt, value) in visit_nums or length(value) > d:
        return
    
    # 현재 값 방문 표시 (계산 횟수, 값)
    visit_nums[(cnt, value)] = True
    # p 횟수 만큼 계산한 경우 최대값 결정
    if cnt == p:
        global result
        # 최대값으로 변경
        result = max(result, value)
        return
    
    # 2 ~ 9 사이의 값을 곱하여 확인
    for v in range(2, 10):
        max_value(d, cnt+1, value * v)

# d, p 입력
d, p = map(int, input().split())

visit_nums = {} # 방문 표시 dict
result = -1     # 결과 저장 변수

# p가 0인 경우 기본값으로 설정
if p == 0:
    result = 1
# p가 1인 경우 9가 최대값
elif p == 1:
    result = 9
# 만들 수 있는 최소값의 자리수가 d를 넘는 경우 -1로 설정
elif length(2 ** p) > d:
    result = -1 
else:
    max_value(d, 0, 1)    

print(result)