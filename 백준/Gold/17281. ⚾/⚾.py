import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input()) # 이닝 수 
score = [list(map(int, input().split())) for _ in range(N)]  # 각 이닝별 결과 

'''
- 1번 선수는 타순 4번(인덱스 3)에 고정
- 나머지 2~9번 선수의 타순 정하기: 순열
- 모든 타순 조합 중 가장 높은 득점 출력 
'''
max_score = 0  # 최대 득점 저장

# 2~9번 선수의 모든 타순 순열 생성
# 이때 (8! = 40320가지) * N 이닝 반복이라 python으로 제출하면 시간 초과 남! pypy로 해야 통과
for order in permutations(range(1, 9), 8):
    # 타순: 1번 선수(0번 인덱스)를 4번째(인덱스 3)에 고정 배치 
    batting_order = list(order[:3]) + [0] + list(order[3:])

    score_sum = 0       # 이번 타순의 총 득점 
    batter_idx = 0      # 현재 타석에 설 타자의 인덱스 (0~8)

    # 각 이닝 진행
    for inning in range(N):
        out = 0   # 아웃 수(현재 이닝 끝나면 초기화)
        b1, b2, b3 = 0, 0, 0  # 1루, 2루, 3루 주자 여부 (0: 없음, 1: 있음)

        # 3아웃 될 때까지 반복  
        while out < 3:
            player = batting_order[batter_idx]   # 현재 타자 번호
            result = score[inning][player]       # 이번 타자의 결과 (0~4)

            # 0: 아웃
            if result == 0:
                out += 1

            # 1 안타: 3루 주자 홈인
            elif result == 1:
                score_sum += b3 
                b1, b2, b3 = 1, b1, b2  # 타자 -> 1루, 1루 -> 2루, 2루 -> 3루

            # 2루타: 2루, 3루 주자 홈인
            elif result == 2:
                score_sum += b2 + b3
                b1, b2, b3 = 0, 1, b1   # 타자 -> 2루, 1루 -> 3루 

            # 3루타: 모든 주자 홈인 
            elif result == 3:
                score_sum += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1    # 타자 -> 3루

            # 홈런: 모든 주자+타자 홈인
            elif result == 4:
                score_sum += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0    # 모든 루 비움

            # 다음 타자 
            batter_idx += 1 
            if batter_idx == 9: # 9번 타자까지 다 치면 다시 1번 타자로 
                batter_idx = 0


    # 이번 타순으로 얻은 점수랑 최대 점수 비교해서 갱신
    max_score = max(max_score, score_sum)

print(max_score)