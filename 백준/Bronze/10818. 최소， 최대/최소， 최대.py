N = int(input())
nums = list(map(int, input().split()))

min_v = nums[0]
max_v = nums[0]
for i in range(N):
    if nums[i] < min_v:
        min_v = nums[i]
    if nums[i] > max_v:
        max_v = nums[i]
print(min_v, max_v)