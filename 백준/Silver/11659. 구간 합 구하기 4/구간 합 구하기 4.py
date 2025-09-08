import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 수의 개수, 합을 구해야 하는 횟수
nums = list(map(int, input().split()))

# 누적합 배열: numbers[0]부터 numbers[i-1]까지의 합 저장
prefix_sum = [0] 
current_sum = 0

# 누적합 계산
for n in nums:
    current_sum = current_sum + n
    prefix_sum.append(current_sum)
    
# M개의 구간합 계산
for _ in range(M):
    i, j = map(int, input().split())
    # i~j 구간합 = j까지 구간합 - i 이전까지의 구간합 
    print(prefix_sum[j] - prefix_sum[i-1])