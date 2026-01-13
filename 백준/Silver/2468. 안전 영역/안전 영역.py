import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
heights = [
    list(map(int, input().split())) for _ in range(n)
]

# 전체 지역에서 가장 높은 곳 찾기
max_h = 0
for row in heights:
    for h in row:
        if h > max_h:
            max_h = h

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS: 특정 높이 h에서 안전 영역 1개를 탐색
def bfs(start_y, start_x, h, visited):
    # 큐에 시작점 삽입
    queue = deque()
    queue.append((start_y, start_x))
    # 시작점 방문 표시
    visited[start_y][start_x] = 1

    # 큐가 빌 때까지 반복
    while queue:
        y, x = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위 안이고, 아직 방문 안 했고, 높이가 h보다 크면 안전 영역
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and heights[ny][nx] > h:
                    # 큐에 삽입
                    queue.append((ny, nx))
                    # 방문 표시
                    visited[ny][nx] = 1

# 안전 영역 개수
max_safe = 0

# 높이(h)를 0부터 max_h까지 반복
for h in range(max_h + 1):
    visited = [[0] * n for _ in range(n)]
    count = 0  # 현재 높이에서의 안전 영역 개수

    # 격자 전체를 이중 for문으로 순회:
    for i in range(n):
        for j in range(n):
            # 아직 방문 안 했고, 높이가 h보다 크면
            if visited[i][j] == 0 and heights[i][j] > h:
                # bfs 탐색하고 카운트 += 1
                bfs(i, j, h, visited)
                count += 1

    # 최댓값 갱신
    if count > max_safe:
        max_safe = count

print(max_safe)