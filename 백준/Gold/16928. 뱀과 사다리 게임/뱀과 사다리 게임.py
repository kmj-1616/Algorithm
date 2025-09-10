import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 사다리 수, 뱀 수

# 사다리와 뱀의 정보는 딕셔너리 만들어서 저장
ladder = {}
snake = {}
for _ in range(n):
    x, y = map(int, input().split())    # 사다리: x -> y (x < y)
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())    # 뱀: u -> v (u > v)
    snake[u] = v

visited = [False]*101   # 방문 표시 배열

q = []  # 큐 생성
# 1번 칸에서 시작, (시작점, 주사위 횟수) 인큐 하고 동시에 방문 표시
q.append((1, 0))
visited[1] = True
# bfs 탐색: 큐가 빌 때까지
while q:
    p, cnt = q.pop(0)
    # 100번 칸에 도착하면 주사위 굴린 횟수 출력하고 종료
    if p == 100:
        print(cnt)
        break
    # 다음 칸 = p + 1~6 주사위 굴려서 나온 수
    for i in range(1, 7):
        next_p = p + i
        # 그 칸이 범위 안이고 아직 방문하지 않은 칸이면 이동할 건데
        if next_p <= 100 and not visited[next_p]:
            # 거기에 사다리가 있으면 찾아서 이동
            if next_p in ladder.keys():
                next_p = ladder[next_p]
            # 거기에 뱀이 있으면 찾아서 이동
            elif next_p in snake.keys():
                next_p = snake[next_p]
            # 거기에 아무것도 없으면 방문 표시, 주사위 횟수 카운트 +1
            if not visited[next_p]:
                visited[next_p] = True
                q.append((next_p, cnt + 1))