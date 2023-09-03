def swap(cnt):
    global answer

    val = int("".join(S))
    if (cnt, val) in visited:
        return
    visited.add((cnt, val))

    if cnt == N:
        answer = max(answer, val)
        return


    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j], S[i]
            swap(cnt + 1)
            S[i], S[j] = S[j], S[i]


T = int(input())

for tc in range(1, T + 1):
    S, N = input().split()

    S = list(S)
    N = int(N)

    visited = set()

    answer = 0

    swap(0)
    print(f"#{tc} {answer}")

