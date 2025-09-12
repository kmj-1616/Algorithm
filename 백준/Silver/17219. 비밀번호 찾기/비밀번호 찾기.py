import sys
input = sys.stdin.readline

m,n = map(int,input().split())
dict = {}
for _ in range(m):
	add, pw = input().split()
	dict[add] = pw
    
for _ in range(n):
	data = input().rstrip()
	print(dict[data])