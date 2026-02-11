import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input().strip()
n = len(s)
# a 개수 
a_total = s.count('a')

# 최소 교환 횟수 초기화 
min_exchange = float('inf')

for i in range(n):
    b_count = 0
    # i부터 a_total만큼 길이 확인
    for j in range(i, i + a_total):
        # 인덱스를 n으로 나눈 나머지
        if s[j % n] == 'b':
            b_count += 1
    
    # 해당 구간의 b 개수가 현재까지의 최소 교환 횟수보다 작으면 갱신
    min_exchange = min(min_exchange, b_count)

print(min_exchange)