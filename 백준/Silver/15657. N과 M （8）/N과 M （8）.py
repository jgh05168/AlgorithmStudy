N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def per(i, output, last):
    if i >= M:
        print(*output)
        return
    for j in range(N):
        # selected[j] = 1
        if arr[j] < last:
            continue
        output.append(arr[j])
        per(i + 1, output, arr[j])
        output.pop()

# selected = [0] * N
per(0, [], 0)