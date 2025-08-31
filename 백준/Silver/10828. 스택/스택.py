import sys 
n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    t = sys.stdin.readline().split() 
    if t[0] == 'push':
        stack.append(t[1])
    elif t[0] == 'pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif t[0] == 'size':
        print(len(stack))
    elif t[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif t[0] == 'top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)