T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split()) # 퍼즐 가로세로 길이, 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]    # NxN 퍼즐

    result = 0   # 단어 들어갈 자리의 수 

    for i in range(N):  
        count = 0   # 흰색(1) 카운트 할 변수

        # 가로 먼저 탐색하는데
        for j in range(N):
            # 1이면 카운트해준다
            if puzzle[i][j] == 1:
                count += 1
            # 만약 0이거나 마지막 인덱스인데
            if puzzle[i][j] == 0 or j == N-1:
                # 카운트가 찾는 K랑 같으면 결과 +1
                if count == K: 
                    result += 1
                count = 0   # 탐색 끝나면 초기화 

        # 세로 탐색 동일하게
        for j in range(N):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == N-1:
                if count == K:
                    result += 1
                count = 0 

    print(f"#{tc} {result}")
