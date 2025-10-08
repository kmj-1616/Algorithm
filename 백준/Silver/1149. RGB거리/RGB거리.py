import sys
input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

# 1번째 집: 이전 집 없음 -> RGB[0] 그대로
dp[0][0] = RGB[0][0]  # R
dp[0][1] = RGB[0][1]  # G
dp[0][2] = RGB[0][2]  # B

# 2번째 집부터 누적 최소 비용 채우기 
# 예: i번째 집이 R이면, 그 집까지 최소 비용은 i-1번째의 G 또는 B 중 적은 비용 + 현재 R 비용
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0] # 현재 R
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1] # 현재 G
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2] # 현재 B

# 마지막 집에서 누적 최소 비용 중 min 값 출력 
print(min(dp[N-1]))
