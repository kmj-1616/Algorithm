L = int(input())
s = input()
M = 1234567891

result = 0
for i in range(L):
    result += (ord(s[i]) - 96) * (31 ** i)

print(result % M)