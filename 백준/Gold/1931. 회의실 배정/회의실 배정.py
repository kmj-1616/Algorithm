import sys
input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
    start, end = map(int, input().split())
    times.append((start,end))
# 끝나는 시간 큰 것부터 정렬, 같으면 시작 시간 기준
times.sort(key=lambda x: (x[1], x[0]))

count = 0   # 회의 최대 개수
last_end = 0    # 마지막 회의 끝난 시간
for start, end in times:
    # 지금 회의가 이전 회의 끝난 시간 이후에 시작하면 카운트하고
    if start >= last_end:
        count += 1
        last_end = end  # 마지막 회의 끝난 시간 갱신

print(count)