import sys
input = sys.stdin.readline

M = int(input())
S = set()   # 집합은 중복된 원소가 없는 set

for _ in range(M):
    txt = input().split()
    cmd = txt[0]

    if cmd == "add":
        x = int(txt[1])
        S.add(x)
    elif cmd == "remove":
        x = int(txt[1])
        S.discard(x)  # remove는 S에 x가 없으면 오류가 난다
    elif cmd == "check":
        # 미리 x 변수를 만들면 check와 toggle의 경우에 indexerror가 난다
        x = int(txt[1])
        if x in S:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        x = int(txt[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cmd == "all":
        S = set(range(1, 21))
    elif cmd == "empty":
        S = set()