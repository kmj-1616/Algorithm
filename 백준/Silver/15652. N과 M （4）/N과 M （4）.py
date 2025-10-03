import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def dfs(n):
    # 종료 조건: M개의 숫자를 모두 선택한 경우 출력
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(n, N+1):  
        # 중복 가능하니까 i부터 시작
        result.append(i)
        dfs(i)  # i부터 다시 시작
        result.pop()  # 백트래킹

# 1부터 시작
dfs(1)
