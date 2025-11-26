N = int(input())
N_cnt = list(map(int,input().split()))
B, C =map(int,input().split())

result=0
for i in range(N):
    N_cnt[i] -= B
    result += 1
    if N_cnt[i] > 0:
        if N_cnt[i] % C ==0:
            result += (N_cnt[i]//C)
        else:
            result += (N_cnt[i]//C+1)

print(result)