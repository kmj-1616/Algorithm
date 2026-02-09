import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

# 초콜릿 반경: 8n - t/12
def get_choco_radius(n, t):
    radius = 8 * n - t / 12
    return max(0, radius)


# 커피 반경: 2n - t*t/79
def get_coffee_radius(n, t):
    radius = 2 * n - (t * t) / 79
    return max(0, radius)


all_data = []

while True:
    line = input().split()
    if not line:
        break

    cmd = line[0]
    time = int(line[1])
    amount = float(line[2]) if len(line) > 2 else 0.0

    # (시간, 명령어, 양)
    all_data.append((time, cmd, amount))

# 시간 순서대로 정렬
all_data.sort()

history = []

for T, cmd, amount in all_data:
    if cmd == 'Chocolate':
        history.append(('Choco', T, amount))
    elif cmd == 'Coffee':
        history.append(('Coffee', T, amount))
    elif cmd == 'Query':
        total_radius = 0

        for item_type, eat_time, n in history:
            t = T - eat_time
            if t < 0:
                continue

            if item_type == 'Choco':
                total_radius += get_choco_radius(n, t)
            else:
                total_radius += get_coffee_radius(n, t)

        # 안전 거리 최소 1 유지, 소수점 첫째 자리까지 출력
        safety_dist = max(1.0, total_radius)
        print(f"{T} {safety_dist:.1f}")