import sys
input = sys.stdin.readline

# NxN 도시, 남길 최대 치킨집 개수 M
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

# 도시를 순회하면서 분류: 1은 집, 2는 치킨집
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# 조합 결과(선택된 치킨집) 저장
result = []
# 최소 치킨 거리 초기값
ans = 1e9

# 현재 조합에 대해 모든 집의 최소 거리 합을 계산하는 함수  
def get_distance():
    total = 0
    # 모든 집에 대해 거리 계산
    for hx, hy in houses:
        dist = 1e9  # 각 집의 최소 거리 초기값
        # 선택된 치킨집 중 가장 가까운 거리 찾기
        for cx, cy in result:
            # 치킨 거리 = |x1 - x2| + |y1 - y2|
            d = abs(hx - cx) + abs(hy - cy)
            dist = min(dist, d)
        total += dist  # 가장 가까운 치킨집 거리 합
    return total

# 조합을 이용해 M개의 치킨집을 선택하는 함수
def recur(cnt, start):
    global ans

    # 종료 조건: M개의 치킨집을 다 선택했으면 
    if cnt == M:
        ans = min(ans, get_distance())  # 도시 치킨 거리 계산하고 최소값 갱신
        return

    # 조합 탐색
    for i in range(start, len(chickens)):
        result.append(chickens[i])    # i번째 치킨집 선택
        recur(cnt + 1, i + 1)    # 다음 인덱스부터 탐색
        result.pop()   # 백트래킹

# 0, 0부터 시작 
recur(0, 0)

print(ans)
