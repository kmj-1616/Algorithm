import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

'''
공간 상태 (matrix)
0: 빈 칸
1~6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치 (공간당 1마리)
'''

# 1️. 초기 설정
# - 아기 상어 크기 = 2
# - 먹은 물고기 수 = 0
# - 총 시간 = 0
# - 9의 위치를 찾아 저장하고, 그 칸을 0으로 변경

# 2️. BFS 탐색: 현재 상어 위치에서 먹을 수 있는 물고기까지 거리 계산할 건데 조건
# - 자신의 크기 이하의 칸만 이동 가능
# - 자기보다 작은 물고기만 먹을 수 있음
#
# BFS 결과:
# - 모든 칸까지의 최단 거리(시간)를 계산
# - 먹을 수 있는 물고기들의 위치랑 거리 저장

# 3️. 먹을 물고기가 여러 마리면 우선순위 적용
#   (1) 가장 가까운 거리
#   (2) 가장 위쪽 (x가 작은 순)
#   (3) 가장 왼쪽 (y가 작은 순)

# 4️. 선택한 물고기로 이동
#   - 이동 거리만큼 시간 += 거리
#   - 먹은 물고기 수 += 1
#   - 해당 칸을 0으로 바꾸고, 상어 위치 갱신

# 5️. 성장 조건
#   - 먹은 물고기 수 == 상어 크기 -> 상어 크기 += 1, 먹은 수 = 0

# 6️. 더 이상 먹을 물고기가 없으면 종료 -> 총 시간 출력


# 방향 우선순위: 위, 왼쪽, 오른쪽, 아래
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 2. 현재 상어 위치에서 BFS로 물고기 탐색 
def bfs(x, y, size):
    visited = [[-1] * N for _ in range(N)]
    q = deque([(x, y)])
    visited[x][y] = 0
    fishes = []

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위 안이고, 아직 방문 안 했고, 상어 크기 이하 칸이면 이동 가능
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if matrix[nx][ny] <= size:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx, ny))

                    # 자기보다 작은 물고기는 먹을 수 있음
                    if 0 < matrix[nx][ny] < size:
                        # (거리, x, y) 저장 -> 나중에 정렬로 우선순위 결정
                        fishes.append((visited[nx][ny], nx, ny))

    # 거리 -> 위쪽 -> 왼쪽 순 정렬
    fishes.sort()
    return fishes


# 1. 아기 상어 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            x, y = i, j
            matrix[i][j] = 0  # 9를 0으로 변경
            break

size = 2    # 초기 상어 크기
eat_count = 0   # 먹은 물고기 수
time = 0    # 총 이동 시간

while True:
    fishes = bfs(x, y, size)

    # 6. 더 이상 먹을 물고기가 없으면 종료 
    if not fishes:
        break
    
    # 3. 정렬된 리스트에서 가장 우선순위 높은 물고기 선택
    dist, nx, ny = fishes[0]

    # 4. 이동
    x, y = nx, ny
    time += dist
    matrix[x][y] = 0
    eat_count += 1

    # 5. 성장
    if eat_count == size:
        size += 1
        eat_count = 0

print(time)
