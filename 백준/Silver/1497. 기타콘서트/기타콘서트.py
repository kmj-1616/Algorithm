import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

guitars = []
for _ in range(n):
    name, can_play = input().split()
    # 'Y'인 곡의 인덱스만 리스트에 추가 
    playable = []
    for i in range(m):
        if can_play[i] == 'Y':
            playable.append(i)
    guitars.append(playable)

max_songs = 0
min_guitars = -1

# 기타 조합 1개~n개 뽑기
for i in range(1, n + 1):
    for comb in combinations(guitars, i):
        # 연주 가능한 곡 체크 
        check = [False] * m
        
        # 선택된 기타들을 하나씩 꺼내서 연주 가능한 곡 표시
        for g_list in comb:
            for song_idx in g_list:
                check[song_idx] = True 
        
        # 연주 가능한 곡의 총합 세기
        count = 0
        for can_do in check:
            if can_do:
                count += 1
        
        # 최대 곡 수, 최소 기타 수 갱신
        if count > 0:
            if count > max_songs:
                max_songs = count
                min_guitars = i
            elif count == max_songs:
                # 같은 곡 수면 더 적은 기타 수 선택
                if min_guitars == -1 or i < min_guitars:
                    min_guitars = i

print(min_guitars)