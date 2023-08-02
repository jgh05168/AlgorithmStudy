T = 10

for tc in range(1, T + 1):
    dump = int(input())

    boxes = list(map(int, input().split()))

    while dump > 0:

        max_val = 0
        max_idx = 0
        min_val = 100
        min_idx = 0

        for idx, val in enumerate(boxes):
            if max_val < val:
                max_val = val
                max_idx = idx
            if min_val > val:
                min_val = val
                min_idx = idx

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        dump -= 1

    max_val = 0
    min_val = 100
    for val in boxes:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val

    print(f'#{tc} {max_val - min_val}')