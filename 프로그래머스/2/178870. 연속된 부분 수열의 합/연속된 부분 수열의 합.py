def solution(sequence, k):
    n = len(sequence)
    answer = [0, n - 1]

    start = 0
    total = 0
    for i in range(n):
        total += sequence[i]
        if k < total:
            while total > k:
                total -= sequence[start]
                start += 1
        if total == k:
            if answer[1] - answer[0] > i - start:
                answer = [start, i]


    return answer