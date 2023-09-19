N, M = map(int, input().split())

def per(i, output):
    if i >= M:
        print(*output)
        return
    for j in range(N):
        output.append(j + 1)
        per(i + 1, output)
        output.pop()

per(0, [])