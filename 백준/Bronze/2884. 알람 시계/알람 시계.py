H, M = map(int, input().split())

if M < 45:
    M += 15
    if H == 0:
        print(23, M)
    else:
        print(H-1, M)
else:
    print(H, M-45)