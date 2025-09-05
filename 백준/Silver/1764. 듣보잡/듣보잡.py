import sys
input = sys.stdin.readline

N, M = map(int, input().split())
no_h = set()
no_s = set()
no_both = []

for _ in range(N):
    no_h.add(input())   
for _ in range(M):
    no_s.add(input())

for name in no_h:   # 듣도 못한 이름이
    if name in no_s:    # 보도 못한 이름 리스트에 있으면
        no_both.append(name)    # 듣보잡 리스트에 추가
no_both.sort()  # 사전순 정렬

print(len(no_both))
print(''.join(no_both), end='')