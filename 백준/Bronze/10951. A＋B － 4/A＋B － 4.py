while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break # 정수가 아닌 수가 입력되면 반복 종료 