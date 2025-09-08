N, K = map(int, input().split())  # N 종류의 동전으로 합 K 만들기
coins = list(int(input()) for _ in range(N))
# 규칙: 큰 동전부터 사용하기 -> 내림차순 정렬
coins.sort(reverse=True)

count = 0 
for coin in coins:
		# 현재 동전이 K보다 작거나 같으면
    if coin <= K:
        count += (K // coin)  # 최대한 많이 사용하고
        K = K % coin  # 나머지 금액 갱신
        
    if K == 0:  # 남은 금액이 없으면 종료 
        break
 
print(count)  # 최소 동전 개수 