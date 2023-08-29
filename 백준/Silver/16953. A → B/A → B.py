def recur(cnt, val):
    global min_cnt
    if min_cnt <= cnt:
        return
    if val > B:
        return
    elif val == B:
        if min_cnt > cnt:
            min_cnt = cnt
    else:
        recur(cnt + 1, val * 2)
        recur(cnt + 1, val * 10 + 1)


min_cnt = 10**9
A, B = map(int, input().split())
recur(1, A)

if min_cnt == 10**9:
    print(-1)
else:
    print(min_cnt)