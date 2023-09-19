N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def per(i, output, idx):
    if i >= M:
        print(*output)
        return
    for j in range(idx, N):
        if not selected[j]:
            selected[j] = 1
            output.append(arr[j])
            per(i + 1, output, j)
            output.pop()
            selected[j] = 0

selected = [0] * N
per(0, [], 0)