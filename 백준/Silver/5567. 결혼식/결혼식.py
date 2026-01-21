import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline

# n: 동기의 수, m: 리스트 길이
n = int(input())
m = int(input())

# 친구 관계를 저장할 인접 리스트
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

# 방문 여부와 상근이로부터의 거리를 저장
# -1은 아직 확인하지 않음, 0은 상근이 본인
distance = [-1] * (n + 1)
distance[1] = 0

# BFS 상근이부터 시작
queue = deque([1])
while queue:
    now = queue.popleft()
    
    # 상근이로부터 거리가 2인 사람의 친구는 초대 대상이 아님
    if distance[now] == 2:
        continue
        
    for next_friend in graph[now]:
        # 아직 방문하지 않은 친구라면
        if distance[next_friend] == -1:
            distance[next_friend] = distance[now] + 1
            queue.append(next_friend)

# 거리가 1 또는 2인 사람의 수 세기
count = 0
for i in range(2, n + 1): # 2번부터 시작 
    if 0 < distance[i] <= 2:
        count += 1

print(count)