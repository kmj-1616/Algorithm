def dfs(v):
    stack = []  # 공백 스택 생성
    stack.append(v)  # 시작 정점 v를 스택에 추가
    visited[v] = True  # 동시에 방문 표시
    count = 0

    # 스택이 빌 때까지 반복 (더 이상 방문할 정점이 없을 때까지)
    while stack:
        v = stack.pop()
        # 현재 정점 v에 연결된 모든 정점을 순회
        for w in graph[v]:
            if not visited[w]:  # 아직 방문하지 않은 정점이면
                visited[w] = True  # 방문 표시하고
                stack.append(w)  # 스택에 추가 (이동)
                count += 1  # 컴퓨터 수 카운트 +1

    return count

n = int(input())  # 컴퓨터의 수
m = int(input())  # 직접 연결된 컴퓨터 쌍의 수

# 그래프 초기화 (컴퓨터 번호가 1부터 시작하니까 n+1)
graph = [[] for _ in range(n + 1)]
# 연결된 컴퓨터 정보 입력받아서 그래프 채우기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 기록할 리스트 False로 초기화)
visited = [False] * (n + 1)

# 1번 컴퓨터에서 dfs 수행
print(dfs(1))