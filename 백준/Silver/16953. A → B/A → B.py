import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())


# BFS
def bfs(n):
    queue = deque([(n, 1)])
    while queue:
        n, count = queue.popleft()

        if n == A:
            return count

        if n < A:
            continue

        if n % 2 == 0:
            queue.append((n // 2, count + 1))

        if str(n)[-1] == '1':
            n = int(str(n)[0:-1])
            queue.append((n, count + 1))

    return -1


result = bfs(B)

print(result)