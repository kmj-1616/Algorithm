import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# -1, 0, 1의 개수를 저장할 변수
cnt_minus = 0
cnt_zero = 0
cnt_plus = 0

def solve(x, y, size):
    global cnt_minus, cnt_zero, cnt_plus
    
    # 첫 번째 칸의 숫자를 기준으로 잡음
    first_num = paper[x][y]
    
    # 현재 영역이 모두 같은 숫자인지 확인
    is_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first_num:
                is_same = False
                break 
        if not is_same:
            break
    
    # 모두 같다면 해당 숫자 카운트
    if is_same:
        if first_num == -1:
            cnt_minus += 1
        elif first_num == 0:
            cnt_zero += 1
        else:
            cnt_plus += 1
            
    # 하나라도 다르면 9개 영역으로 쪼개서 재귀 호출
    else:
        new_size = size // 3
        # 3x3으로 9번 호출
        for i in range(3):
            for j in range(3):
                solve(x + i * new_size, y + j * new_size, new_size)

# 시작
solve(0, 0, n)

# 출력
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)