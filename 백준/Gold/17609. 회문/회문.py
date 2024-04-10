'''
회문인지(0), 유사회문인지(1), 일반 문자열인지(2) 판별

문자열의 길이 <= 100000

풀이 :
1. 투포인터로 접근
2. 만약 앞 뒤 문자열이 같지 않다면
    2-1. 두 문자열을 각각 빼고 진행해본다.
    2-2. 만약 빼고 진행한 경우 중 한 번이라도 회문이 나오면 유사회문으로 인식
    2-3. 둘 다 아니라면 일반 문자열로 인식

'''

import sys
input = sys.stdin.readline

def findPel(cnt, sidx, eidx, mid):
    if cnt == 2:    # 두 번 들어온 경우
        return cnt

    for idx in range(mid):
        if sidx + idx >= eidx - idx:
            return cnt
        if input_string[sidx + idx] != input_string[eidx - idx]:
            # 각각 한 번씩 돌아가면서 최솟값 return(유사회문 or 일반문자열 판별 여부)
            return min(findPel(cnt + 1, sidx + idx + 1, eidx - idx, mid),
                       findPel(cnt + 1, sidx + idx, eidx - idx - 1, mid))

    return cnt


t = int(input())
for _ in range(t):
    input_string = input().rstrip()

    print(findPel(0, 0, len(input_string) - 1, len(input_string) // 2))
