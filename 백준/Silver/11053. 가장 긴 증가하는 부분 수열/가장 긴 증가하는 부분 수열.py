import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N   # 자기 자신만으로도 길이 1

# i를 기준으로 앞쪽 j 탐색
for i in range(1, N):
    for j in range(0, i):
        if nums[j] < nums[i]:      # 증가하는 부분 수열 조건
            dp[i] = max(dp[i], dp[j] + 1)

result = max(dp)
print(result)
