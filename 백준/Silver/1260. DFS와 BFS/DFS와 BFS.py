import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 인접 리스트
adj_lst = [[] for _ in range(N+1)]
for a, b in edges:
    adj_lst[a].append(b)
    adj_lst[b].append(a)    # 양방향

# 방문 가능 점이 여러 개면 번호 작은 순부터 -> 오름차순 정렬 
for i in range(1, N+1):
    adj_lst[i].sort()

# DFS (재귀)
visited = [0]*(N+1)
dfs_route = []

def dfs(node):
    visited[node] = 1
    dfs_route.append(node)
    for next_node in adj_lst[node]:
        if visited[next_node] == 0:
            dfs(next_node)

dfs(V)
print(*dfs_route)

# BFS
visited = [0]*(N+1)
bfs_route = []

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        bfs_route.append(now)
        for next_node in adj_lst[now]:
            if visited[next_node] == 0:
                queue.append(next_node)
                visited[next_node] = 1

bfs(V)
print(*bfs_route)