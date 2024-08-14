'''
매일 아침 한 줄로 선다.
-> 그냥 index에 맞게 채워넣으면 된다.
만약 현재 자리에 누가 이미 있고, 나보다 작으면 다음 빈자리로 이동
만약 자리에 없으면 값 저장

뒤에서부터 자리에 삽입하기
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n
for i in range(n, 0, -1):
    sequence = arr[i - 1]
    if not ans[sequence]:
        ans[sequence] = i
    else:
        if ans[sequence] < i:
            move_person = i
        else:
            move_person = ans[sequence]
        for j in range(n - 1, sequence - 1, -1):
            if ans[j]:
                move_idx = j
                while j < n and not ans[j + 1]:
                    ans[j], ans[j + 1] = 0, ans[j]
        ans[sequence] = i

print(*ans)