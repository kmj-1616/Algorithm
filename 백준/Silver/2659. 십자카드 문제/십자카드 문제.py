import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

nums = list(map(int, input().split()))

# 입력받은 카드의 시계수(clock_num) 구하기
candidates = []
for i in range(4):
    # 시계 방향으로 회전시키면서 4개 숫자 만들기
    rotated = nums[i:] + nums[:i]
    num_val = int("".join(map(str, rotated)))
    candidates.append(num_val)

# 그 중 가장 작은 수가 시계수
clock_num = min(candidates)

# 1111부터 clock_num까지 시계수가 몇 개인지 세기
count = 0
for i in range(1111, clock_num + 1):
    s_num = str(i)

    # 0은 나타날 수 없으므로 건너뜀
    if '0' in s_num:
        continue

    # 현재 숫자 i의 시계수를 직접 구해서 i가 시계수인지 확인
    num_list = list(map(int, s_num))
    rotated_nums = []
    for j in range(4):
        rotated = num_list[j:] + num_list[:j]
        val = int("".join(map(str, rotated)))
        rotated_nums.append(val)

    # i로 만든 조합 중에 최솟값이 i면 i 자체가 시계수이다 
    if min(rotated_nums) == i:
        count += 1

print(count)