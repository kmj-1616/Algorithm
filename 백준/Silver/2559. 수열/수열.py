import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 처음 k개 합 저장
total = sum(nums[:k])
max_total = total

# 인덱스 k부터 처음 합에서 왼쪽 값 빼고 오른쪽 값 더하면서 합 구하기
for i in range(k, n):
    total = total - nums[i-k] + nums[i]
    
    # 최댓값 갱신
    if total > max_total:
        max_total = total

print(max_total)
