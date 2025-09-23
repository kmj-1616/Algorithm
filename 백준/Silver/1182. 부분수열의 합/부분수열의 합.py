def dfs(idx, total):
    global cnt

    # 종료 조건: 모든 원소를 다 본 경우
    if idx == N:
        # 합이 S가 되면 개수 세기
        if total == S:
            cnt += 1
        return

    # 현재 원소를 선택하는 경우
    dfs(idx + 1, total + nums[idx])

    # 현재 원소를 선택하지 않는 경우
    dfs(idx + 1, total)


N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
dfs(0, 0)

# 공집합 제외
if S == 0:
    cnt -= 1

print(cnt)