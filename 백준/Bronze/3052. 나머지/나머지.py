result = []

for i in range(10):
    num = int(input())
    if num % 42 not in result:
        result.append(num % 42)
print(len(result))