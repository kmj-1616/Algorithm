n = int(input())

room = 1 # 방 개수
count = 1 # 라인 수

while room < n:
    room += 6 * count # 해당 라인의 방 개수 계산
    count += 1 # 라인 수 증가

print(count) 