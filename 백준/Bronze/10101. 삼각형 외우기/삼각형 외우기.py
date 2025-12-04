import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b == c:
        print('Equilateral')
    else:
        if (a == b) or (b == c) or (c == a):
            print('Isosceles')
        else:
            print('Scalene')
else:
    print('Error')
    