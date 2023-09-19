N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def per(i, output):
    if i >= M:
        print(*output)
        return
    for j in range(N):
        # selected[j] = 1
        output.append(arr[j])
        per(i + 1, output)
        output.pop()

# selected = [0] * N
per(0, [])