N = int(input())    # 지방의 수 
request = list(map(int, input().split()))    # 각 지방의 예산 요청금액
M = int(input())    # 총 예산

# 1. 모든 요청이 배정될 수 있는 경우(M 이하인 경우)
if sum(request) <= M:
    print(max(request))  # 요청금액 중 최댓값 출력
    
# 2. 모든 요청이 배정될 수 없는 경우
else:    
    left = 0                # 최소 상한액
    right = max(request)    # 최대 상한액
    result = 0              # 가능한 최대 총 예산 저장 

    # 이진 탐색으로 상한액 계산하기 
    while left <= right:
        mid = (left + right) // 2  # 중간값(상한액 후보)
        total = 0                  # 배정 예산 합 초기화
        
        for r in request:
            # 각 지방의 요청금액이 mid보다 크면 mid만큼만 배정
            if r > mid:
                total += mid
            # mid 이하면 요청금액 그대로 배정 
            else:
                total += r

        # 배정 예산 합이 M 이하면 상한액을 더 높여도 됨(오른쪽에서 탐색)
        if total <= M:
            result = mid
            left = mid + 1
        # 배정 예산 합이 M 초과하면 상한액을 낮춰야 함(왼쪽에서 탐색)
        else:
            right = mid - 1

    # 가능한 최대 상한액 출력
    print(result)
