import sys
from itertools import permutations

input = sys.stdin.readline

# 주어진 타순으로 경기를 진행해서 총 점수를 반환하는 함수
def play_game(order, n, score_data):
    score_sum = 0
    batter_idx = 0
    
    for inning_scores in score_data:
        out = 0
        b1, b2, b3 = 0, 0, 0  # 각 루 주자 여부 
        
        while out < 3:
            result = inning_scores[order[batter_idx]]
            
            if result == 0:
                out += 1
            elif result == 1:
                score_sum += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score_sum += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score_sum += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif result == 4:
                score_sum += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            
            # 다음 타자로 이동 
            batter_idx += 1
            if batter_idx == 9:
                batter_idx = 0
                
    return score_sum

def solve():
    n = int(input())
    # 각 이닝별 선수들의 결과 
    score_data = [list(map(int, input().split())) for _ in range(n)]
    
    max_score = 0
    
    # 1번 선수(인덱스 0) 빼고 나머지 8명(1~8번 인덱스)의 순열 생성
    for p in permutations(range(1, 9), 8):
        # 타순: 1번 선수(0)를 4번째(인덱스 3)에 고정
        order = list(p[:3]) + [0] + list(p[3:])
        
        # 경기 실행
        current_score = play_game(order, n, score_data)
        
        # 최대 점수 갱신
        if current_score > max_score:
            max_score = current_score
            
    print(max_score)

solve()