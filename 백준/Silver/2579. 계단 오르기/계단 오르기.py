import sys
input = sys.stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)]

# 계단이 1개 이하일 때
if N == 1:
    print(stair[0])
# 계단이 2개일 때
elif N == 2:
    print(stair[0] + stair[1])
else:
    DP = [0] * N
    DP[0] = stair[0]                         # 첫 계단
    DP[1] = stair[0] + stair[1]              # 두 계단 연속 밟기
    DP[2] = max(stair[0] + stair[2], stair[1] + stair[2])  # 세 번째 계단까지

    # 네 번째 계단부터
    for i in range(3, N):
        DP[i] = max(
            DP[i-2] + stair[i],              # 한 칸 건너뛰고 밟기
            DP[i-3] + stair[i-1] + stair[i]  # 두 칸 연속 밟기
        )

    print(DP[-1])
