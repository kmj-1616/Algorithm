N = int(input())
	
fact = 1
for i in range(2, N + 1):	# 팩토리얼
    fact *= i

fact = str(fact)	# 문자열로 바꾸기

cnt = 0 # 0 개수 카운트 
for i in range(1, len(fact)):
    if fact[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)