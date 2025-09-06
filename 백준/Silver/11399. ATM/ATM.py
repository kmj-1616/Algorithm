import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

total = 0
cur = 0
for n in nums:
    cur += n    # 누적합 계산
    total += cur    # 최종합 계산 

print(total)
