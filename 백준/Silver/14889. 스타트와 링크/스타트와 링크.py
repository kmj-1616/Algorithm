import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# 방문 체크 배열 
visited = [False] * n
min_diff = 1e9

def dfs(depth, idx):
    global min_diff
    
    # 종료 조건: n/2명을 모두 뽑았을 때
    if depth == n // 2:
        start_team_score = 0
        link_team_score = 0
        
        # 팀 점수 계산
        for i in range(n):
            for j in range(n):
                # i와 j가 모두 스타트 팀인 경우
                if visited[i] and visited[j]:
                    start_team_score += s[i][j]
                # i와 j가 모두 링크 팀인 경우
                elif not visited[i] and not visited[j]:
                    link_team_score += s[i][j]
        
        # 차이 최솟값 갱신
        min_diff = min(min_diff, abs(start_team_score - link_team_score))
        return

    # 백트래킹 
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1) # 다음 사람 선택 
            visited[i] = False

dfs(0, 0)
print(min_diff)