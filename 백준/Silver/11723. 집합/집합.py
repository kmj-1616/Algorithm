import sys

input = sys.stdin.readline

def func_set():
    m = int(input())
    s = set()

    for _ in range(m):
        line = input().split()
        command = line[0]
        
        # 숫자 연산 
        if len(line) > 1:
            x = int(line[1])
            
            if command == "add":
                s.add(x)
            elif command == "remove":
                s.discard(x) 
            elif command == "check":
                print(1 if x in s else 0)
            elif command == "toggle":
                if x in s:
                    s.remove(x)
                else:
                    s.add(x)
        
        # 숫자 필요 없는 연산
        else:
            if command == "all":
                # 1부터 20까지의 집합으로 바꾸기
                s = set(range(1, 21))
            elif command == "empty":
                s.clear()

func_set()