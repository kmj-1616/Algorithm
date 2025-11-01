N = int(input())

pil = []
for _ in range(N):
    L, H = map(int, input().split())
    pil.append((L, H))
# 왼쪽에 있는 기둥부터 정렬
pil.sort()

# 가장 높은 기둥(최대 높이)과 인덱스 찾기
ans = 0      # 최종 면적
i = 0
for p in pil:
    if p[1] > ans:  # 더 높은 기둥 발견하면 갱신
        ans = p[1]
        idx = i     # 가장 높은 기둥의 인덱스 저장
    i += 1

# 왼쪽 부분
max_h = pil[0][1]  # 시작 기둥의 높이로 초기화

# 첫 번째부터 순회하면서, 
for i in range(idx):
    # 다음 기둥이 현재 최대 높이보다 높으면
    if max_h < pil[i+1][1]:
        # (현재 높이 * 현재까지의 너비)로 면적을 더하고, 기준 높이 갱신
        ans += max_h * (pil[i+1][0] - pil[i][0])
        max_h = pil[i+1][1]
    # 아니면 현재 높이로 면적 계산하고 더하기
    else:
        ans += max_h * (pil[i+1][0] - pil[i][0])

# 오른쪽 부분 
# 맨 오른쪽 기둥부터 왼쪽으로 똑같이 계산
max_h = pil[-1][1]  # 오른쪽 끝 기둥의 높이로 초기화

for i in range(N-1, idx, -1):
    if max_h < pil[i-1][1]:
        ans += max_h * (pil[i][0] - pil[i-1][0])
        max_h = pil[i-1][1]
    else:
        ans += max_h * (pil[i][0] - pil[i-1][0])

print(ans)
