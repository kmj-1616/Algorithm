import sys
input = sys.stdin.readline

L, P = map(int, input().split())
nums = list(map(int, input().split()))

ans = []
for i in range(5):
    ans.append(nums[i] - L*P)

print(*ans)