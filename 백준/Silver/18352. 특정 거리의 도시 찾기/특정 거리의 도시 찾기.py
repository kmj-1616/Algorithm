import sys
from collections import deque

input = sys.stdin.readline
# 도시 개수, 도로 개수, 찾는 거리, 출발 도시
n, m, k, x = map(int, input().split())

# 도시 1번부터 n번까지 각 도시에 연결된 도로 정보 인접 리스트
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# -1은 아직 방문하지 않은 도시
distance = [-1] * (n + 1)
# 출발 도시 x에서 x까지 최단 거리는 항상 0
distance[x] = 0

# BFS 탐색
queue = deque([x])
while queue:
    now = queue.popleft()
    
    # 거리가 k면 탐색 종료 
    if distance[now] == k:
        continue

    # 현재 도시에서 갈 수 있는 모든 이웃 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 현재 도시까지의 거리 + 1을 저장
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 찾은 도시가 있는지 확인
found = 0
# 모든 도시를 순회하며 최단 거리가 k인 도시 찾기
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = 1

# 거리가 k인 도시가 하나도 없으면 -1
if found == 0:
    print(-1)