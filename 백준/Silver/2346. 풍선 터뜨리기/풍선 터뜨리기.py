import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# [풍선 번호, 이동 숫자] 저장
q = deque()
for i in range(n):
    q.append([i + 1, numbers[i]])

answer = []

while q:
    # 현재 타겟 풍선을 터뜨리기
    balloon = q.popleft()
    num, move = balloon[0], balloon[1]
    answer.append(num)

    # 남은 풍선이 없으면 종료
    if not q:
        break

    # move만큼 이동
    if move > 0:
        # 양수면 오른쪽으로 이동 (move-1)
        for _ in range(move - 1):
            q.append(q.popleft())
    else:
        # 음수면 왼쪽으로 이동 (절댓값)
        for _ in range(abs(move)):
            q.appendleft(q.pop())

print(*(answer))