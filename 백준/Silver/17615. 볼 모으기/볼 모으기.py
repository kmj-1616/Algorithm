import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
balls = list(input().strip())

# 최소 이동 횟수 저장
answer = []

# 1. 오른쪽으로 빨간색 보내기
cnt = 0
red = 0
for i in range(n):
    if balls[i] == "R":
        red += 1
    elif balls[i] == "B":
        # 파란색 만나면 지금까지 쌓인 빨간색 옮김
        cnt += red
        red = 0
answer.append(cnt)

# 2. 오른쪽으로 파란색 보내기
cnt = 0
blue = 0
for i in range(n):
    if balls[i] == "B":
        blue += 1
    elif balls[i] == "R":
        # 빨간색 만나면 지금까지 쌓인 파란색 옮김
        cnt += blue
        blue = 0
answer.append(cnt)

# 3. 왼쪽으로 빨간색 보내기
balls.reverse()

cnt = 0
red = 0
for i in range(n):
    if balls[i] == "R":
        red += 1
    elif balls[i] == "B":
        cnt += red
        red = 0
answer.append(cnt)

# 4. 왼쪽으로 파란색 보내기
cnt = 0
blue = 0
for i in range(n):
    if balls[i] == "B":
        blue += 1
    elif balls[i] == "R":
        cnt += blue
        blue = 0
answer.append(cnt)

print(min(answer))