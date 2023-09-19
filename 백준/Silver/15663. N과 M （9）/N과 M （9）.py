N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def per(i, output):
    if i >= M:
        ans.add(tuple(output))
        return
    for j in range(N):
        if not selected[j]:
            selected[j] = 1
            output.append(arr[j])
            per(i + 1, output)
            output.pop()
            selected[j] = 0

ans = set()
selected = [0] * N
per(0, [])


for i in range(len(ans)):
    print(*list(ans)[i])