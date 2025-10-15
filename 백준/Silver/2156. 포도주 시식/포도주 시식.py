import sys
input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]

# 포도주 잔이 1개: 첫 잔만 마시면 됨
if N == 1:
    print(wine[0])
# 포도주 잔이 2개: 두 잔 다 마시는 게 최댓값
elif N == 2:
    print(wine[0] + wine[1])
else:
    DP = [0] * N  # DP[i] = i번째 잔까지 고려했을 때의 최댓값

    DP[0] = wine[0]                  # 첫 번째 잔만 마실 수 있음
    DP[1] = wine[0] + wine[1]        # 두 번째 잔까지는 연속으로 마셔도 됨

    # 세 번째 잔부터 
    for i in range(2, N):
        # 3가지 경우 중 최대값 선택
        DP[i] = max(
            DP[i-1],                        # 현재 잔을 안 마시는 경우
            DP[i-2] + wine[i],              # i-2까지 마시고 i번째 마시는 경우
            DP[i-3] + wine[i-1] + wine[i]   # i-1, i번째 잔을 연속으로 마시는 경우
        )

    # 마지막 잔까지 고려한 최댓값
    print(DP[-1])
