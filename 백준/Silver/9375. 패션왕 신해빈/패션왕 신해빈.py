import sys
input = sys.stdin.readline

T = int(input())  
for _ in range(T):
    clothes = {}   # 의상 종류별로 아이템을 저장할 딕셔너리
    count = 1
    n = int(input())  # 의상 수

    # 의상 종류별로 분류
    for _ in range(n):
        name, type = input().rstrip().split()
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]
    
    # 각 의상 종류마다 경우의 수 계산
    for i in clothes:
        count *= (len(clothes[i]) + 1)
	
    # 아무것도 안 입는 경우 제외하고 출력
    print(count - 1)
