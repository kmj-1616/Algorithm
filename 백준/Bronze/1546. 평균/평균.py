n = int(input())
scores = list(map(int, input().split()))

m = max(scores)
print(sum(score/m*100 for score in scores)/n)