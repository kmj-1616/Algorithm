import sys

def validation_num(nums):
    total = 0
    for num in nums:
        total += num ** 2
    return total % 10

nums = list(map(int, sys.stdin.readline().split()))
print(validation_num(nums))