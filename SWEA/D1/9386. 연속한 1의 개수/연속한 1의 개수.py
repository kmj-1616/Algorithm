T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = input()

    # 1의 개수 기록할 변수
    count = 0
    # 1의 개수 중 최댓값 기록할 변수
    max_count = 0
    # 수열을 순회 
    for i in arr: 
        # 1이면 개수 추가
        if i == '1': 
            count += 1
            # 현재 카운트보다 최대 카운트가 크면 갱신 
            if count > max_count:
                max_count = count 
        # 1이 아니면 (0이면) 횟수 세지 않음 
        else: 
            count = 0

    print(f"#{test_case} {max_count}")