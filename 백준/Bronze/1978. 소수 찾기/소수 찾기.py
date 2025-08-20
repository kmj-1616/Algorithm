N = int(input())
nums = list(map(int, input().split()))

count = 0
for num in nums:
    error = 0
    if num > 1:    # 1보다 큰 수 중에 (0, 1은 소수가 아님)
        for i in range(2, num):
            if num % i == 0:    # 2부터 num-1까지의 숫자로 나누어떨어지면
                error += 1      # 소수가 아님
        
        if error == 0:    # 나누어떨어지지 않았으면 소수니까 개수 세기 
            count += 1
    
print(count)
    