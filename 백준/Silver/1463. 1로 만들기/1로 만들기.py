import sys
input = sys.stdin.readline

N = int(input())

def recur(n, count):
    global min_count
    # 종료 조건: 1이 되면 최소 연산 횟수 출력
    if n == 1:
        min_count = min(min_count, count)
        return

    # 가지치기: 이미 최소보다 count가 크면 중단
    if count >= min_count:
        return

    # 연산
    if n % 3 == 0:
        recur(n // 3, count + 1)
    if n % 2 == 0:
        recur(n // 2, count + 1)

    recur(n - 1, count + 1)

min_count = 1e9
recur(N, 0)
print(min_count)
