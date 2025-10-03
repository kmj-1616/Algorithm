import sys
input = sys.stdin.readline

N, M = map(int, input().split())  
nums = sorted(list(map(int, input().split())))  # 입력받은 숫자들을 정렬
visited = [0] * N   # 방문 체크
result = []

def dfs():
    # 종료 조건: M개의 숫자를 모두 고르면 출력
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    # N개의 숫자를 하나씩 확인
    for i in range(N):
        if not visited[i]:  # 아직 방문 안 했으면
            visited[i] = 1       # 표시
            result.append(nums[i])  # 수열에 추가
            dfs()                   # 다음 숫자 선택
            result.pop()            # 백트래킹
            visited[i] = 0      # 표시 해제

# DFS 시작
dfs()
