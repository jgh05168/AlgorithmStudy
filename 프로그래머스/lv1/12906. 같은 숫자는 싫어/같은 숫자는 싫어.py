def solution(arr):
    answer = []
    answer.append(arr[0])
    arr.pop(0)
    for i in arr:
        if i == answer[-1]:
            continue
        answer.append(i)
    return answer