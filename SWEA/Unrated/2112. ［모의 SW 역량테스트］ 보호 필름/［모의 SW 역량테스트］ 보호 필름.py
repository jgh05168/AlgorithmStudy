'''
두께 x 가로크기 의 보호필름, 각 셀들은 특성 A 또는 B
세로방향 셀들의 특성이 중요
모든 세로 방향에 대해 동일한 특성의 셀들이 k개 이상 연속으로 있는 경우만 성틍검사 통과

약물 : 막(row) 별로 투입 가능
    - 모든 셀들이 하나의 특성으로 변경돼ㅣㄴ다.
성능 검사를 통과하는 최소 약품 투입 횟수 찾기

풀이:
r < 13 | c < 20
최소로 넣어보면서 통과한다면 종료

조합 & 구현
'''

def dfs(cnt, s_idx, film):
    if cnt == total:
        # 검사 시작
        for c in range(w):
            cell_pr = film[0][c]
            tmp_cell = 1
            pass_cell = False
            for r in range(1, d):
                if film[r][c] == cell_pr:
                    tmp_cell += 1
                else:
                    cell_pr = film[r][c]
                    tmp_cell = 1
                if tmp_cell >= k:
                    pass_cell = True
                    break
            if not pass_cell:
                break
        else:
            # 통과를 한 경우이다.
            return True, cnt
        return False, -1
    else:
        for idx in range(s_idx + 1, d):
            bef_film = film[idx]
            film[idx] = [0] * w
            get_ans, val = dfs(cnt + 1, idx, film)
            if get_ans:
                return True, val
            film[idx] = [1] * w
            get_ans, val = dfs(cnt + 1, idx, film)
            if get_ans:
                return True, val
            film[idx] = bef_film
    return False, -1


t = int(input())
for tc in range(1, t + 1):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]

    # 처음부터 모두 선택하는 경우가 존재
    for total in range(d):
        get_ans, ans = dfs(0, -1, film)      # 현재 선택 갯수, idx
        if get_ans:
            break
    print(f'#{tc} {ans}')