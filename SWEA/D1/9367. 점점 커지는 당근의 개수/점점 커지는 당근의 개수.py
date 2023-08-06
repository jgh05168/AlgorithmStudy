T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    karrots = list(map(int, input().split()))

    cnt = 1
    max_cnt = 0
    max_weight = karrots[0]
    for idx in range(1, len(karrots)):
        if karrots[idx] > max_weight:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
            max_weight = karrots[idx]
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
            max_weight = karrots[idx]
            
            
    print(f'#{tc} {max_cnt}')