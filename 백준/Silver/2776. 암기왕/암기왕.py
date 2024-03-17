'''
풀이 :
1. 수첩 1에 적어놓은 숫자들 오름차순 정렬
2. for문 돌면서 현재 숫자가 있는지 없는지 탐색한 다음 있으면 1, 없으면 0 출력

1000000log1000000 = 6000000
'''

import sys
input = sys.stdin.readline

def bin_search(start, end, num):
    if start >= end:
        return 0

    else:
        mid = (start + end) // 2
        if note_1[mid] == num:
            return 1
        elif note_1[mid] > num:
            return bin_search(start, mid, num)
        else:
            return bin_search(mid + 1, end, num)

T = int(input())
for _ in range(T):
    n = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()

    m = int(input())
    note_2 = list(map(int, input().split()))

    for num in note_2:
        print(bin_search(0, n, num))

