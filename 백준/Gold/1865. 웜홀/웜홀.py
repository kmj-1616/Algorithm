import sys
input = sys.stdin.readline

INF = int(1e9)

def bellman_ford(start, N):
    distance = [INF for i in range(N + 1)]
    distance[start] = 0

    # N번 반복 (N번째에서 갱신이 일어나면 음수 사이클이 존재하는 것)
    for i in range(N):
        for cur_node, next_node, edge_cost in edges:
            # 출발 노드가 아직 도달 불가능한 경우 패스
            # if distance[cur_node] == INF:
                # continue

            # 더 짧은 경로를 찾은 경우 갱신
            if distance[next_node] > distance[cur_node] + edge_cost:
                # N번째 라운드에서도 값이 갱신되면 음수 사이클 존재
                if i == N - 1:
                    return True
                distance[next_node] = distance[cur_node] + edge_cost
    return False

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []

    # 양방향 도로
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    # 단방향 웜홀 (음수 가중치)
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    result = bellman_ford(1, N)

    if result == True:
        print("YES")
    else:
        print("NO")
