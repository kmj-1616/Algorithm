import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # (0, 0)에서 시작
    queue = deque([(0, 0)])
    
    while queue:
        now_x, now_y = queue.popleft()
        
        # 상하좌우 확인
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            
            # 미로 범위를 벗어나는지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽인지 확인
            if graph[nx][ny] == 0:
                continue
            
            # 처음 방문하는 길인 경우만 탐색 
            if graph[nx][ny] == 1:
                # 이전 칸의 거리 값 + 1을 현재 칸에 저장
                graph[nx][ny] = graph[now_x][now_y] + 1
                queue.append((nx, ny))
                
    # 최단 거리 값 반환
    return graph[n-1][m-1]

n, m = map(int, input().split())

# 미로 정보
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

print(bfs())