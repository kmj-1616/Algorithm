t = int(input())

for _ in range(t):
    # hxw 호텔, n번째 손님 방 배정 
    h, w, n = map(int, input().split())
    # 방 번호는 n을 h로 나눈 몫 + 1
    room = n//h + 1
    # 층수는 n을 h로 나눈 나머지 
    floor = n % h
    # 그런데 n이 h의 배수여서 0층이 되면 
    if floor == 0:
        room = n//h
        floor = h
    print(floor*100 + room)