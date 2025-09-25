import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0   # 시작점은 거리 0

    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 이동
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = x + di, y + dj
            
            # 범위 안이고, 아직 방문하지 않은 경우
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                if graph[ni][nj] == 0: 
                    visited[ni][nj] = 0   # 갈 수 없으면 0
                elif graph[ni][nj] == 1:
                    visited[ni][nj] = visited[x][y] + 1  # 거리 갱신
                    queue.append((ni, nj))

# 목표 지점(값이 2인 곳)에서 BFS 시작
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

# 출력: 원래 0인 곳은 0, 그 외는 거리 출력
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
