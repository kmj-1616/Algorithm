# 스위치 상태 바꾸는 함수
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

n = int(input())    # 스위치 개수
switch = [0] + list(map(int, input().split()))		# [0] + 각 스위치의 처음 상태 (인덱스 1부터)
student = int(input())		# 학생 수
for _ in range(student):
    sex, num = map(int, input().split())	# 성별, 받은 수
    # 남자면
    if sex == 1:
        for i in range(num, n+1, num):		# 받은 수의 배수 번호인 스위치의 상태를 변경
            change(i)
    # 여자면
    else:
        change(num) # 먼저 스위치 상태 바꾸기
        for k in range(n//2):   # 중심부터 좌우 1칸씩 대칭인지 확인
            # 대칭이 아니면 멈추기
            if num + k > n or num - k < 1 :
                break
            # 대칭이면 둘 다 상태 바꾸기
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

# 최종 상태는 1번부터 마지막까지 한 줄에 20개씩 출력                
for i in range(1, n+1):
    print(switch[i], end = " ")
    if i % 20 == 0:
        print()