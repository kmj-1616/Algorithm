import sys
imput = sys.stdin.readline

N = int(input())
members = [input().split() for _ in range(N)]

# 나이순으로 정렬하기 
members.sort(key=lambda x: int(x[0]))

for age, name in members:
    print(age, name)
