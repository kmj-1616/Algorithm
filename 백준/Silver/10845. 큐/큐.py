import sys

n = int(sys.stdin.readline())
text = [sys.stdin.readline() for _ in range(n)]

queue = []

# 명령 하나씩 보면서 큐의 동작 수행
for t in text:
    # push
    if 'push' in t.split()[0]:
        queue.append(t.split()[1])
    # pop
    elif 'pop' in t:
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    # size
    elif 'size' in t:
        print(len(queue))
    # empty
    elif 'empty' in t:
        if queue:
            print(0)
        else:
            print(1)
    # front
    elif 'front' in t:
        if queue:
            print(queue[0])
        else:
            print(-1)
    # back
    elif 'back' in t:
        if queue:
            print(queue[-1])
        else:
            print(-1)