T = int(input())   # 테스트 케이스 개수

for _ in range(T):
    data = input().strip()   # 괄호 문자열
    N = len(data)

    pair = {'(': ')'}    # 괄호 짝
    top = -1
    stack = [0] * (N + 1)

    result = 'YES'  # VPS면 YES 출력
    for x in data:
        if x == '(':    # 여는 괄호면 push
            top += 1
            stack[top] = x
        elif x == ')':  # 닫는 괄호면 pop
            if top == -1:   # 스택이 비어 있으면 오류
                result = 'NO'
                break
            else:
                y = stack[top]
                if pair[y] != x:  # 짝이 안 맞으면 오류
                    result = 'NO'
                    break
                top -= 1    # 짝이 맞으면 pop

    if top != -1:   # 끝났는데 스택에 남아있으면 오류
        result = 'NO'

    print(result)
