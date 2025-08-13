num = list(map(int, input().split()))

# 오름차순이랑 내림차순 기록
asc = True
desc = True


for i in range(1,8):
    if num[i-1] < num[i]:
        desc = False
    elif num[i-1] > num[i]:
        asc = False

        if not asc and not desc:
            print('mixed')
            break

if asc:
    print('ascending')
elif desc:
    print('descending')