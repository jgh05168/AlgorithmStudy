'''
미사일을 최소로 사용해서 모든 폭격 미사일을 요격
- 2차원 공간으로 이뤄짐
- a나라의 폭격 미사일은 (s, e)로 주어진 직선 형태
- b나라는 특정 x좌표에서 y축에 수평이 되도록 미사일 발사
    - a나라의 미사일을 관통하여 요격 가능
    - s 또는 e에서 발사하는 미사일은 요격 불가능

풀이:
구간 : 0 ~ 10**8
-> 그리디
1. 끝나는 지점으로 오름차순
2. while(!stack) 돌며 pop
3. 초기값과 마지막값 비교
    - (max(n_start, start), min(n_end, end))
    - 만약 n_end <= start: cnt++, start, end 업데이트

'''

import sys
input = sys.stdin.readline

def solution(targets):
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    s, e = targets.pop()
    while targets:
        ns, ne = targets.pop()
        # 종료 조건
        if ne <= s:
            answer += 1
            s, e = ns, ne
        else:
            if ns > s:
                s = ns
            if ne < e:
                e = ne
    answer += 1
    
    return answer