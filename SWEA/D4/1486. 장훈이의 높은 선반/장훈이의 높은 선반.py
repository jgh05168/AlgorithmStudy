
def calc(staff, val):
    global min_h
    if staff >= N:
        if min_h > val and val >= B:
            min_h = val
        return
    if min_h < val:
        return
    calc(staff + 1, val + staffs[staff])
    calc(staff + 1, val)

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    staffs = list(map(int, input().split()))
    selected = [0] * N
    min_h = 10000 * N
    calc(0, 0)
    print(f'#{tc} {min_h - B}')


