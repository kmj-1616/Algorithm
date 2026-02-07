import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 인접 리스트
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

# 거리 저장 리스트 (방문하지 않은 곳은 -1)
dist = [-1] * (n + 1)

def bfs(start):
    queue = deque([start])
    dist[start] = 0 # 시작점 0
    
    while queue:
        now = queue.popleft()
        
        for next_node in lst[now]:
            # 아직 방문하지 않은 곳이면 
            if dist[next_node] == -1:
                # 이전 헛간 거리 + 1 저장 
                dist[next_node] = dist[now] + 1
                queue.append(next_node)

bfs(1)

max_val = max(dist)    # 1번 헛간으로부터의 최대 거리
target_node = dist.index(max_val)    # 최대 거리를 가진 가장 작은 헛간 번호
count = dist.count(max_val)    # 최대 거리에 있는 헛간의 총 개수

print(target_node, max_val, count)