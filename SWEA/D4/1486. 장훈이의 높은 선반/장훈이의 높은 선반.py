from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # N: 점원 수, B: 선반 높이
    heights = list(map(int, input().split()))   # 점원들 키
    S = sum(heights)    # N=1 이면 B=S, N>=2면 B=탑을 만든 점원 키 합

    # 목표: B 이상 탑 중에 탑의 높이와 B의 차이가 가장 작은 것 찾기
    min_diff = 987654321
    # 키로 만들 수 있는 조합을 찾고
    for i in range(1, N+1):
        for c in combinations(heights, i):
            # 그중에 합이 B 이상이면, 최소 높이 차이 갱신
            if sum(c) >= B:
                min_diff = min(min_diff, sum(c)-B)

    print(f'#{tc} {min_diff}')