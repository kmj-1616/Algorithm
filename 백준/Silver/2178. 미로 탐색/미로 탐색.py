import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 미로 정보 입력 (공백 없이 붙어 있으므로 strip()으로 문자열을 숫자로 분해)
graph = [list(map(int, input().strip())) for _ in range(N)]

# 이동 방향
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(start_i, start_j):
    q = deque()
    q.append((start_i, start_j))    # 시작점 인큐
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            # 범위 안이고, 이동 가능한 길(1)이면
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 1:
                graph[ni][nj] = graph[i][j] + 1  # 거리 갱신
                q.append((ni, nj))

# BFS 시작점 
bfs(0, 0)

# 도착점 (N-1,M-1)까지의 거리 출력
print(graph[N-1][M-1])
