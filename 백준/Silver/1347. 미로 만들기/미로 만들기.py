import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
action = input().rstrip()

arr = [['#']*100 for _ in range(100)]

# 시계방향 (남서북동)
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
curr_dir = 0  # 처음엔 남쪽

# 가운데에서 시작
y, x = 50, 50
arr[y][x] = '.'  # 시작점 표시

# 범위를 구하기 위한 변수 초기화
min_y, max_y = y, y
min_x, max_x = x, x

for a in action:
    if a == 'R':
        # 오른쪽으로 90도 회전
        curr_dir = (curr_dir + 1) % 4
    elif a == 'L':
        # 왼쪽으로 90도 회전
        curr_dir = (curr_dir - 1) % 4
    elif a == 'F':
        # 보고 있는 방향으로 한 칸
        y += dy[curr_dir]
        x += dx[curr_dir]
        # 이동 경로 표시
        arr[y][x] = '.'

        # 지도의 크기를 결정하기 위해 현재 좌표의 최솟값/최댓값 갱신
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)

    # print(f"{a} -> ({y}, {x})")

# 범위만큼만 출력
for i in range(min_y, max_y + 1):
    print("".join(arr[i][min_x: max_x + 1]))