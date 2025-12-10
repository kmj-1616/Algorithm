import sys
input = sys.stdin.readline

word = input().rstrip()
cnt = 0
for w in word:
    if w in ['a','e','i','o','u']:
        cnt += 1
print(cnt)