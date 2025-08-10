T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))
    
    for _ in range(M):
        i, j = map(int, input().split())

        # 중심 i를 기준으로 거리 1부터 j까지 확인
        for k in range(1, j+1):
            left = i - k - 1 # 왼쪽 인덱스
            right = i + k - 1 # 오른쪽 인덱스 
            # 주어진 돌을 벗어나면 중단 
            if left < 0 or right >= N:
                break
            # 양쪽 같은 색이면 뒤집기
            if rocks[left] == rocks[right] == 1:
                rocks[left] = 0
                rocks[right] = 0
            elif rocks[left] == rocks[right] == 0:
                rocks[left] = 1
                rocks[right] = 1
    
    print(f"#{tc}", *rocks)

