import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 분할 정복을 이용한 거듭제곱
def multi(a, n):
    # 지수가 1이면 a % c 반환
    if n == 1:  
        return a % c
    else:
        tmp = multi(a, n // 2)  # 지수를 절반으로 나눠서 재귀 호출

        if n % 2 == 0:  # 지수가 짝수면
            return (tmp * tmp) % c  # (a^(n//2) * a^(n//2)) % c
        else:  # 지수가 홀수면
            return (tmp * tmp * a) % c  # (a^(n//2) * a^(n//2) * a) % c

print(multi(a, b))
