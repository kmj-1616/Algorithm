import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

def bfs(start):
    deq = deque([start])
    while deq:
        node = deq.popleft()
        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = node
                deq.append(adj)

bfs(1)

for i in range(2, N + 1):
    print(visited[i])
