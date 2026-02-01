import sys
input = sys.stdin.readline

n, d = map(int, input().split())

shortcuts = []
for _ in range(n):
    start, end, dist = map(int, input().split())
    # 역주행 불가=도착점이 d 이하(end <= d), 실제 거리(end-start)보다 짧으면 지름길 추가 
    if end <= d and (end - start) > dist:
        shortcuts.append((start, end, dist))

# dp[i]: 시작점(0)부터 i 지점까지 오는 데 필요한 최소 거리
dp = [i for i in range(d + 1)]

for i in range(d + 1):
    # 직진 확인: (현재까지의 최솟값)과 (이전 칸에서 1km 걸어온 값) 중 작은 값 선택
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)
    
    # 지름길 확인: 현재 위치에서 시작하는 지름길이 있으면
    for start, end, dist in shortcuts:
        if i == start:
            # (지름길 도착지의 기존 최솟값)과 (현재 위치까지의 거리 + 지름길 거리) 중 작은 값 선택
            if dp[end] > dp[i] + dist:
                dp[end] = dp[i] + dist

print(dp[d])