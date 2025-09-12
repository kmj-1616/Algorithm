T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    cnt = 0
    max_cnt = 0
    for i in range(N):
        # 1이 나오면 길이 세고 최댓값 갱신
        if arr[i] == '1':
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        # 0 나와서 끊기면 카운트 초기화 
        else:
            cnt = 0

    print(f'#{tc} {max_cnt}')