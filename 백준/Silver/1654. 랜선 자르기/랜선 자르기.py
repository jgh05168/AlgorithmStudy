'''
이진탐색
'''

def BinarySearch(start, end):
    while start <= end:
        mid = (start + end) // 2
        if not mid:
            break

        total = 0
        for i in range(K):
            total += lans[i] // mid

        if total >= N:
            start = mid + 1
        else:
            end = mid - 1

    return end


K, N = map(int, input().split())
lans = []
for i in range(K):
    lans.append(int(input()))

start = 0
end = max(lans)

max_lan = BinarySearch(start, end)
print(max_lan)