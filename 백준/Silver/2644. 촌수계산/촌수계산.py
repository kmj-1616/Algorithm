from collections import deque

def bfs(start, end, n):
    visited = [0] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = 0   # 시작 노드의 촌수는 0

    while q:
        node = q.popleft()
        if node == end:
            return visited[node]  # end까지의 촌수 반환
        for next_node in graph[node]:
            if visited[next_node] == 0 and next_node != start:  # 아직 방문 안 했으면
                visited[next_node] = visited[node] + 1     # 부모의 촌수 + 1
                q.append(next_node)
    return -1   # 연결이 안 된 경우

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]    # 인접 리스트
for _ in range(m):
    x, y = map(int, input().split())    # 부모, 자식
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a, b, n))