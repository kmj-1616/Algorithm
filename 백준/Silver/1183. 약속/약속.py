import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())    # n명
# 기다리는 시간 = 뒤 도착 - 앞 도착 = a-b
# 약속을 t만큼 미루면, 기다리는 시간의 합 = |a+t-b| => |t-(b-a)|의 합
# 이게 최소가 되려면: t와 (b-a) 사이의 거리 찾기 = 중앙값
times = []
for _ in range(n):
    a, b = map(int, input().split())
    times.append(b-a)

# 중앙값 찾기 위해 정렬
times.sort()

# n이 홀수면: 중앙값(무조건 1개)에서 전체 거리의 합이 최소가 됨
if n % 2 != 0:
    print(1)
# n이 짝수면:
else:
    # 가운데 두 값((인덱스 n//2-1 과 n//2) 사이 범위에 있으면 전체 거리의 합이 최소가 됨
    # 두 중앙값 사이의 정수 개수 계산
    count = times[n//2] - times[n//2-1] + 1
    print(count)