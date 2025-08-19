while True:
    sides = list(map(int, input().split()))    # 리스트로 입력받기
    if sum(sides) == 0:    # 값이 모두 0이면 반복 종료 
        break              # 입력받자마자 체크해야 함: 마지막에 하면 wrong이 출력됨 
    sides.sort()    # 오름차순으로 정렬: 빗변의 길이는 가장 긴 거
    if sides[0]**2 + sides[1]**2 == sides[2]**2:    # 피타고라스 정리 성립하면 직각 
        print("right")
    else:
        print("wrong")