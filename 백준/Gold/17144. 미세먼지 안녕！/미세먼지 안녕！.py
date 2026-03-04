import sys

input = sys.stdin.readline

def diffuse(r, c, board, purifier):
    # 미세먼지가 인접한 4방향으로 확산되는 함수
    new_board = [[0] * c for _ in range(r)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                amount = board[x][y] // 5
                count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    # 범위 안이고 공기청정기 위치가 아니면 확산
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        new_board[nx][ny] += amount
                        count += 1
                new_board[x][y] += (board[x][y] - (amount * count))
            elif board[x][y] == -1:
                new_board[x][y] = -1
    return new_board

def clean_air(r, c, board, purifier):
    # 1. 위쪽 공기청정기 (반시계 방향)
    top = purifier[0]
    # 아래로 당기기
    for i in range(top - 1, 0, -1): board[i][0] = board[i-1][0]
    # 왼쪽으로 당기기
    for i in range(c - 1): board[0][i] = board[0][i+1]
    # 위로 당기기
    for i in range(top): board[i][c-1] = board[i+1][c-1]
    # 오른쪽으로 당기기
    for i in range(c - 1, 1, -1): board[top][i] = board[top][i-1]
    board[top][1] = 0 # 공기청정기에서 나온 깨끗한 공기

    # 2. 아래쪽 공기청정기 (시계 방향)
    bottom = purifier[1]
    # 위로 당기기
    for i in range(bottom + 1, r - 1): board[i][0] = board[i+1][0]
    # 왼쪽으로 당기기
    for i in range(c - 1): board[r-1][i] = board[r-1][i+1]
    # 아래로 당기기
    for i in range(r - 1, bottom, -1): board[i][c-1] = board[i-1][c-1]
    # 오른쪽으로 당기기
    for i in range(c - 1, 1, -1): board[bottom][i] = board[bottom][i-1]
    board[bottom][1] = 0 # 공기청정기에서 나온 깨끗한 공기

def solve():
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    
    # 공기청정기 위치 찾기 (항상 1열에 위치)
    purifier = []
    for i in range(r):
        if board[i][0] == -1:
            purifier.append(i)
            
    # T초 동안 반복
    for _ in range(t):
        board = diffuse(r, c, board, purifier)
        clean_air(r, c, board, purifier)
        
    # 남은 미세먼지 합 계산 (-1인 공기청정기 2곳은 제외해야 함)
    answer = sum(sum(row) for row in board) + 2
    print(answer)

# 실행
solve()