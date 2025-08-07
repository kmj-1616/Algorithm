T = int(input())

for test_case in range(1, T+1):
    R, S = input().split()

    for i in range(len(S)):
        print(int(R)*S[i], end='') # end = '' : 옆으로 출력 
    print() # 개행 