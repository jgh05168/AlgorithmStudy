T = int(input())

for tc in range(1, T + 1):
    s = input()
    s_rvs = list(s)
    s_rvs.reverse()

    s_reverse = ''.join(s_rvs)
    ans = 0

    if s == s_reverse:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')