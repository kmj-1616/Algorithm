import sys

input = sys.stdin.readline

def get_unheard_unseen():
    # n: 듣도 못한 사람 수, m: 보도 못한 사람 수
    n, m = map(int, input().split())
    
    # 듣도 못한 사람들을 set 저장 
    unheard = set()
    for _ in range(n):
        unheard.add(input().strip())
    
    # 보도 못한 사람들을 확인하면서 교집합 찾기
    result = []
    for _ in range(m):
        name = input().strip()
        if name in unheard:
            result.append(name)
    
    # 사전순 정렬
    result.sort()
    
    print(len(result))
    for name in result:
        print(name)

get_unheard_unseen()