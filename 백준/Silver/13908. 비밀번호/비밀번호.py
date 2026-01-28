import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
known = list(map(int, input().split())) if m > 0 else []

# 필수 숫자 포함 여부 
visited = [False] * 10
for x in known:
    visited[x] = True

answer = 0
def dfs(depth, cnt):
    global answer
    
    # 종료 조건: n자리 비밀번호가 완성되었을 때
    if depth == n:
        # 기억나는 숫자(m개)를 모두 포함했으면 정답 카운트
        if cnt == m:
            answer += 1
        return

    for i in range(10):
        # 이번에 고른 숫자가 필수 숫자고, 아직 이번 조합에서 카운트되지 않았으면 
        if visited[i]:
            visited[i] = False  
            dfs(depth + 1, cnt + 1)
            visited[i] = True   
        else:
            # 일반 숫자거나 이미 카운트된 필수 숫자면 cnt 유지
            dfs(depth + 1, cnt)

dfs(0, 0)

print(answer)