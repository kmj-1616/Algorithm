import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_dict = {}
name_dict = {}
for i in range(N):
    name = input().rstrip()
    # 번호를 key로 하는 dict에 이름 저장
    num_dict[i + 1] = name    
    # 이름을 key로 하는 dict에 번호 저장 
    name_dict[name] = i + 1

for _ in range(M):
    quest = input().rstrip()
    # 문제가 숫자 타입이면 이름, 아니면 번호를 정답으로 출력 
    if (quest.isdecimal()):
        print(num_dict[int(quest)])
    else:
        print(name_dict.get(quest))