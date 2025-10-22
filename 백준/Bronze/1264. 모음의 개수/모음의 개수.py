while True:
    cnt = 0
    N = input()
    if N == "#":
        break
    for i in N:
        if i in "aeiouAEIOU":
            cnt += 1
    print(cnt)