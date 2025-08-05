nums = [] # 숫자 입력받을 리스트 

for i in range(9):
    n = int(input()) # 9개의 서로 다른 자연수 입력받고
    nums.append(n) # 리스트에 추가

max_n = nums[0] # 최댓값 초기화
max_idx = 0     # 최댓값 위치 
for j in range(9): # 현재 값과 최댓값 비교하며 기록
    if nums[j] > max_n:
        max_n = nums[j]
        max_idx = j

print(max_n)
print(max_idx + 1) # 인덱스는 0부터 시작하기 때문에 +1 
