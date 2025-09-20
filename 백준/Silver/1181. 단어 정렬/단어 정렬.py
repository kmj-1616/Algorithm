import sys
input = sys.stdin.readline

N = int(input())
data = [input().strip() for _ in range(N)]

# 중복 제거
data = list(set(data))
# 정렬: 길이가 짧은 것부터, 같으면 사전 순
data = sorted(data, key=lambda x: (len(x), x))

for x in data:
    print(x)