import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # DP 배열
    DP = [[0] * N for _ in range(2)]

    # 1번째 열
    DP[0][0] = arr[0][0]    # 위쪽 스티커 선택
    DP[1][0] = arr[1][0]    # 아래쪽 스티커 선택
    
    # 2번째 열 스티커 선택하면 바로 직전 열의 대각선 반대쪽 스티커만 선택 가능함 
    if N > 1:
        DP[0][1] = arr[0][1] + DP[1][0]
        DP[1][1] = arr[1][1] + DP[0][0]

    # 3번째 열부터는 점화식 
    # i열에서 위쪽/아래쪽 스티커 고르면 같은 행 i-1번째 빼고 두 경우 중에 최대 값 고름 
    for i in range(2, N):
        DP[0][i] = arr[0][i] + max(DP[1][i-1], DP[1][i-2])
        DP[1][i] = arr[1][i] + max(DP[0][i-1], DP[0][i-2])
    
    print(max(DP[0][N-1], DP[1][N-1]))
