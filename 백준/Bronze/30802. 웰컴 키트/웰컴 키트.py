n = int(input())
num = list(map(int, input().split()))
t, p = map(int, input().split())

count = 0
for i in range(6):
    if num[i]%t != 0:
        count += num[i]//t + 1
    elif num[i]%t == 0:
        count += num[i]//t
print(count)
print(sum(num)//p, sum(num)%p)