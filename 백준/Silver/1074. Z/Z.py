def rec(value, row, col, n):
    if n == 0:
        return value
    else:
        srow, erow = row[0], row[1]
        scol, ecol = col[0], col[1]
        rmid = (srow + erow) // 2
        cmid = (scol + ecol) // 2
        # 1사분면
        if srow <= r <= rmid and scol <= c <= cmid:
            return rec(value + (4 ** (n - 1)) * 0, (srow, rmid), (scol, cmid), n - 1)
        # 2사분면
        elif srow <= r <= rmid and cmid + 1 <= c <= ecol:
            return rec(value + (4 ** (n - 1)) * 1, (srow, rmid), (cmid + 1, ecol), n - 1)
        # 3사분면
        elif rmid + 1 <= r <= erow and scol <= c <= cmid:
            return rec(value + (4 ** (n - 1)) * 2, (rmid + 1, erow), (scol, cmid), n - 1)
        # 4사분면
        elif rmid + 1 <= r <= erow and cmid + 1 <= c <= ecol:
            return rec(value + (4 ** (n - 1)) * 3, (rmid + 1, erow), (cmid + 1, ecol), n - 1)

N, r, c = map(int, input().split())

print(rec(0, (0, 2**N - 1), (0, 2**N - 1), N))
