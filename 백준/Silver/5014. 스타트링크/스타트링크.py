import sys
from collections import deque

def bfs(s):
    q = deque([s])
    visited[s] = 1  # 시작층 방문

    while q:
        s = q.popleft()

        # 종료 조건: 목표층에 도달하면 버튼 누른 횟수 출력
        if s == G:
            print(count[G])
            return

        # 위로 U층, 아래로 D층 이동
        for i in (s + U, s - D):
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[s] + 1
                q.append(i)

    # 큐가 빌 때까지 목표층을 못 찾으면
    print('use the stairs')

# F(최대층), S(시작층), G(목표층), U(위로), D(아래로)
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())

# 방문 여부와 버튼 누른 횟수 저장용 리스트
visited = [0] * (F + 1)
count = [0] * (F + 1)

# BFS 실행
bfs(S)
