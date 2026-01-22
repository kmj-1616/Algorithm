import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
# + - * / 개수
operator = list(map(int, input().split()))

# 최댓값, 최솟값 초기화 
max_val = -1e9
min_val = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global max_val, min_val
    
    # 종료 조건: 모든 숫자를 다 사용했을 때
    if depth == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    # 각 연산자가 남아있으면 재귀 호출
    if plus > 0:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        # 음수를 양수로 나눌 때의 조건 처리
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

# 0번째 숫자는 이미 사용, total은 첫 번째 숫자
dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])

print(int(max_val))
print(int(min_val))