T = int(input())

for _ in range(1, T+1):
    string = input()
    stack = []
    score = 0   # 점수 기록

    for ch in string:    # OX 결과를 확인하는데
        if ch == 'O':    # O면 push하고
            stack.append(ch)
            score += len(stack) # 스택 길이(O의 개수)만큼 점수 추가
        else:       # X면 스택 비우고 다음 확인  
            stack.clear()
    print(score)