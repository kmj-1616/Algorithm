from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, input().split())    # 정점 개수, 간선 개수 
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 요소의 개수
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        # bfs 끝나면 카운트 
        bfs(graph, i, visited) 
        count += 1

print(count)