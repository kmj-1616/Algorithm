import sys
input = sys.stdin.readline

N = int(input())   # 삼각형의 크기 (줄 수)
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))  # dp에 저장

# 두 번째 줄부터 위의 값들을 참고해서 최댓값 누적합 계산
for i in range(1, N):  # i: 현재 행
    for j in range(0, i+1):  # j: 현재 행의 열 인덱스
        if j == 0:
            # 맨 왼쪽 끝은 바로 위 값만 더할 수 있음
            dp[i][j] += dp[i-1][j]
        elif j == i:
            # 맨 오른쪽 끝은 바로 왼쪽 위 값만 더할 수 있음
            dp[i][j] += dp[i-1][j-1]
        else:
            # 그 외는 위쪽 두 값 중 큰 값을 더함
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

# 마지막 줄(dp[N-1])에서 가장 큰 값이 전체 최대 경로의 합
print(max(dp[N-1]))
