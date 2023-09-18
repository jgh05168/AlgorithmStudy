'''
기본적인 이진검색 + parametric search(결정알고리즘)
만족하는 H 찾기

'''

def find_H(mid):
    H = trees[mid]
    temp = 0
    for i in range(mid + 1, N):
        temp += trees[i] - H

    if temp == M:
        return 2
    elif temp > M:
        return 1
    else:
        return 0

def BinarySearch(trees):
    start, end = 0, N - 1
    low, high = 0, 0

    while start <= end:
        mid = (start + end) // 2
        isvalid = find_H(mid)
        if isvalid == 2:
            return trees[mid]
        elif isvalid == 1:
            start = mid + 1
            low = trees[mid]
        else:
            end = mid - 1
            high = trees[mid]

    visited = []
    sidx = low
    # H 구하기
    while low <= high:
        mid_h = (low + high) // 2
        if mid_h in visited:
            return mid_h

        visited.append(mid_h)
        temp = 0
        if trees[mid] < mid_h:
            mid += 1
        for i in range(mid, N):
            temp += trees[i] - mid_h

        if temp == M:
            return mid_h
        elif temp > M:
            low = mid_h
        else:
            high = mid_h

    return 0

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

H = BinarySearch(trees)
print(H)