N, K = map(int, input().split())

# 이항계수 공식: N! / K!(N-K!)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(N) // (factorial(K) * factorial(N - K)))