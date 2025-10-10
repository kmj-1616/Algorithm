import sys
input = sys.stdin.readline

def dfs():
    # 종료 조건: 수열의 길이가 m이 되면 출력
    if len(result) == m:
        print(*result)
        return
    used = 0 # 직전에 사용한 숫자 저장
    for i in range(n):
        # 방문하지 않았고, 이전에 같은 숫자를 사용하지 않았으면 탐색
        if not visited[i] and used != nums[i]:
            visited[i] = True
            result.append(nums[i])
            used = nums[i]
            dfs()
            visited[i] = False
            result.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split()))) # 숫자 정렬해서 입력받기 (사전순)
visited = [False] * n
result = []

dfs()