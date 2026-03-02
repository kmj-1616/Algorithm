import sys

input = sys.stdin.readline

def get_min_coin_count():
    # n: 동전 종류 수, k: 목표 금액
    n, k = map(int, input().split())
    
    # 동전 가치 입력 (오름차순)
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    
    count = 0
    
    # 큰 가치의 동전부터 확인하기 위해 리스트를 뒤집어서 순회
    for i in range(n - 1, -1, -1):
        coin_value = coins[i]
        
        # 현재 동전으로 목표 금액을 채울 수 있으면
        if k >= coin_value:
            # k를 현재 동전으로 나눈 몫이 사용된 동전 개수
            count += k // coin_value
            # 남은 금액은 나머지
            k %= coin_value
            
        # k가 0이 되면 더 이상 계산할 필요 없음
        if k == 0:
            break
            
    print(count)

get_min_coin_count()