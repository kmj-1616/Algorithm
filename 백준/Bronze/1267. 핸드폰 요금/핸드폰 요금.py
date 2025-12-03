import sys
input = sys.stdin.readline

# 영식 Y 30초에 10원
# 민식 M 60초에 15원

n = int(input())
times = list(map(int, input().split()))
y_cost = 0
m_cost = 0

for i in times:
    y_cost += (i//30+1)*10
    m_cost += (i//60+1)*15

if y_cost == m_cost:
    print("Y M", y_cost)
elif y_cost > m_cost:
    print("M", m_cost)
else:
    print("Y", y_cost)