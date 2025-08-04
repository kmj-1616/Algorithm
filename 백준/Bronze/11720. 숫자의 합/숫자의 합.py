N = int(input())
number = input()

# 합을 기록할 변수 
total = 0
for i in range(N): # 문자열을 인덱스로 접근 
    total += int(number[i]) # 하나씩 total에 더해주기  
print(total)