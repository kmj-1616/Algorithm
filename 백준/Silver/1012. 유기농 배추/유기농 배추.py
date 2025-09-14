import sys
sys.setrecursionlimit(10000)   # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def dfs(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:   # 상하좌우 탐색
        nx, ny = x + dx, y + dy
        # 범위 안이고 배추가 있으면
        if 0 <= nx < M and 0 <= ny < N and land[ny][nx] == 1:
            # 0 바꿔서 방문 처리하고 인접한 배추 계속 탐색하기
            land[ny][nx] = 0
            dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 개수
    land = [[0]*M for _ in range(N)]    # MxN 땅
    for _ in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1  # 좌표에 배추 1 표시 (x, y 바꿔서 해주기)

    count = 0   # 지렁이 마리 수
    # 지렁이는 인접한 다른 배추로 이동 가능하기 때문에, 모여 있는 배추 그룹 수를 세면 된다
    for x in range(M):
        for y in range(N):
            # 배추 있으면 인접한 배추들 방문 표시하고 지렁이 카운트 1
            if land[y][x] == 1:
                dfs(x, y)
                count += 1

    print(count)