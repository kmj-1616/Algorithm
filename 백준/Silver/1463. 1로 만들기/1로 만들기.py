import sys

input = sys.stdin.readline

def make_one():
    n = int(input())
    
    # dp[i]는 숫자 i를 1로 만드는 데 필요한 최소 연산 횟수
    # 0부터 n까지 담아야 하므로 n+1 크기로 생성
    dp = [0] * (n + 1)
    
    # 2부터 n까지 반복하며 최솟값 갱신
    for i in range(2, n + 1):
        # 1. 먼저 1을 빼는 경우 (기본값)
        # i에서 1을 뺀 i-1의 결과값에 연산 횟수 1을 더함
        dp[i] = dp[i-1] + 1
        
        # 2. 2로 나누어떨어지는 경우, 1번 결과와 비교하여 최솟값 선택
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
            
        # 3. 3으로 나누어떨어지는 경우, 현재 결과와 비교하여 최솟값 선택
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
            
    print(dp[n])

# 함수 실행
make_one()