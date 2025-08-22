import sys

N = int(sys.stdin.readline())
counts = [0] * 10001  # 숫자 범위가 1~10000

for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(1, 10001):
    if counts[i] > 0:
        for _ in range(counts[i]):
            sys.stdout.write(f"{i}\n")
