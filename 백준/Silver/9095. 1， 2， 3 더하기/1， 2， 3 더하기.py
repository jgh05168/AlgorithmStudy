def rec(i):
    global cnt
    if i >= n:
        if i == n:
            cnt += 1
        return
    else:
        for j in range(1, 4):
            rec(i + j)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    rec(0)
    print(cnt)