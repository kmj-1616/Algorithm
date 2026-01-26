import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
positions = list(map(int, input().split()))

q = deque([i + 1 for i in range(n)])

answer = 0
for i in positions:
    while True:
        # 찾는 숫자가 맨 앞에 있으면 꺼내고 다음 타겟으로 이동
        if q[0] == i:
            q.popleft()
            break
        else:
            # 현재 큐에서 찾는 숫자의 인덱스가 중간보다 앞에 있는지 확인
            if q.index(i) <= len(q) // 2:
                # 중간보다 앞이거나 같으면 왼쪽으로 한 칸씩 이동
                while q[0] != i:
                    q.append(q.popleft())
                    answer += 1
            else:
                # 중간보다 뒤면 오른쪽으로 한 칸씩 이동
                while q[0] != i:
                    q.appendleft(q.pop())
                    answer += 1

print(answer)