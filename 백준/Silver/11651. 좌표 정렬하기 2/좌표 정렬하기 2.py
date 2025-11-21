import sys
input = sys.stdin.readline

T = int(input())
nums =[]
for _ in range(T) :
    nums.append(list(map(int, input().split())))

nums.sort(key=lambda x : (x[1], x[0]))

for i in range(len(nums)) :
    print(nums[i][0], nums[i][1])