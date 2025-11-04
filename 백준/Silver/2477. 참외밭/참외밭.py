k = int(input())
width = []
height = []
total = []

for i in range(6):
    dir, len = map(int, input().split())
    if dir == 1 or dir ==2:
        width.append(len)
        total.append(len)
    else:
        height.append(len)
        total.append(len)


maxHeightIndex = total.index(max(height))
maxWidthIndex = total.index(max(width))

small1 = abs(total[maxHeightIndex-1] - total[(maxHeightIndex-5 if maxHeightIndex == 5 else maxHeightIndex +1)])
small2 = abs(total[maxWidthIndex-1] - total[(maxWidthIndex-5 if maxWidthIndex == 5 else maxWidthIndex +1)])


print((max(height) * max(width) - small1 * small2) * k)