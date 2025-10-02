import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 숫자 범위(1~N), M: 선택할 숫자 개수
result = []  

def dfs(n):
    # 종료 조건: M개의 숫자를 모두 선택한 경우 출력
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(n, N+1):
        # 결과에 없으면 
        if i not in result:
            # 저장하고
            result.append(i)
            # 다음 숫자 선택 (오름차순)
            dfs(i + 1)
            # 백트래킹 
            result.pop()

# 1부터 시작
dfs(1)
