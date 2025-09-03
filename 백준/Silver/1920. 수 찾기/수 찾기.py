import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))    # list로 하면 시간 초과 남 
M = int(input())
nums = list(map(int, input().split()))

# nums의 수들이 A에 존재하는지 확인해야 함
for num in nums:
    if num in A:
        print(1)
    else:
        print(0)