import sys
input = sys.stdin.readline

N = int(input())    # 정점 개수 
adj_mat = [list(map(int, input().split())) for _ in range(N)]    # 인접 행렬 구성

# 결과 저장할 행렬 (초기값 0)
result = [[0]*N for _ in range(N)]

# DFS 
def dfs(start, node, visited):
    for next_node in range(N):
        # 경로가 있고 아직 방문 안 했으면
        if adj_mat[node][next_node] == 1 and not visited[next_node]:
            visited[next_node] = 1    # 방문 표시
            result[start][next_node] = 1   # 경로 표시 
            dfs(start, next_node, visited)    # 다음 정점

# 각 정점마다 DFS 탐색
for i in range(N):
    visited = [0] * N
    dfs(i, i, visited)

for row in result:
    print(' '.join(map(str, row)))
