T = int(input())

def dfs(month, val):
    global min_v
    if month > 12:
        if min_v > val:
            min_v = val
        return
    else:
        # 한달 / 하루 중 최소
        dfs(month + 1, val + min(prices[1], schedules[month] * prices[0]))
        # 3달치
        dfs(month + 3, val + prices[2])

for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    schedules = [0] + list(map(int, input().split()))

    min_v = prices[-1]
    dfs(1, 0)

    print(f'#{tc} {min_v}')