import sys
import heapq
input = sys.stdin.readline
 
N = int(input())
q = []
 
for _ in range(N):
    x = int(input())
 
    if x > 0:
        heapq.heappush(q, x)
    else:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))