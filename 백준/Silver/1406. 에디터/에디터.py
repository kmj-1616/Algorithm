import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

# 커서 왼쪽 스택
left = list(input().strip())
right = []  # 오른쪽 스택

m = int(input())  # 명령어 개수
for _ in range(m):
    command = input().split()

    # L: 커서를 왼쪽으로 옮김 (left의 마지막 문자를 right로 이동)
    if command[0] == 'L' and left:
            right.append(left.pop())

    # D: 커서를 오른쪽으로 옮김 (right의 마지막 문자를 left로 이동)
    elif command[0] == 'D' and right:
            left.append(right.pop())

    # B: 커서 왼쪽 문자 삭제 (left에서 pop)
    elif command[0] == 'B' and left:
            left.pop()

    # P $: 문자를 커서 왼쪽에 추가 (left에 append)
    elif command[0] == 'P':
        left.append(command[1])

# 왼쪽 스택은 순서 그대로, 오른쪽 스택은 뒤집어서 합치기
print("".join(left) + "".join(reversed(right)))