import sys
input = sys.stdin.readline

# 식을 '-' 기준으로 나눈다
susik = list(input().strip().split('-'))

# 결과값 저장
result = 0

# 맨 처음 항(첫 번째 '-') 앞에 있는 부분은 모두 더해준다.
first = list(susik[0].split('+'))
for num in first:
    result += int(num)

# 그 뒤의 항들은 괄호로 묶어 전부 빼준다.
# '-' 뒤에 나오는 수들은 각각 '+'로 나뉘어 있더라도 전부 한꺼번에 빼야 최솟값이 됨
for i in range(1, len(susik)):
    temp = list(susik[i].split('+'))
    for num in temp:
        result -= int(num)

print(result)
