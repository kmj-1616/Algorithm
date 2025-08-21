n1, n2 = map(int, input().split())

# 최대공약수 (유클리드 호제법)
# a와 b를 나눈 나머지(a%b)를 구해서 a <- b, b <- a%b로 계속 갱신
# b가 0이 되면, 그때의 a가 최대공약수 
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

# 최소공배수
# a와 b의 곱을 최대공약수로 나눈 값 
def lcm(a, b):
    return a*b // gcd(a, b)

print(gcd(n1, n2))
print(lcm(n1, n2))