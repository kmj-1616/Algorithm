import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))  # 중복 제거 + 정렬

result = []

def backtracking(idx):
    # 종료 조건: result에 들어간 숫자가 m개면 출력
    if len(result) == m:
        print(*result)
        return
    
    # idx부터 탐색
    for i in range(idx, len(nums)):
        result.append(nums[i])
        backtracking(i)  # 같은 수 다시 사용 가능
        result.pop()     # 백트래킹

# 0부터 시작
backtracking(0)
