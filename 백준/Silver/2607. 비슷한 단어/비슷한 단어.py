'''
1. 두 단어가 같은 종류의 문자열로 이루어져 있ㅇㅁ
2. 같은 문자는 같은 개수만큼 있다.

첫번째 단어와 비슷한 단어가 몇 개 있는지

풀이:
하나 차이면 쌉가능임
아니라면, 불가능
해시맵 사용하기

'''

import sys
input = sys.stdin.readline
N = int(input())
target = list(input().rstrip()) # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(N-1):
    compare = target[:]
    word = input().rstrip() # 새로운 단어
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)