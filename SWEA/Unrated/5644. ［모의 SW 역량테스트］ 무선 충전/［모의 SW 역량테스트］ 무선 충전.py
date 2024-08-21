'''
BC정보 : 위치, 충전 범위, 성능
BC의 충전 범위가 c일 때, BC와의 거리가 c 이하라면, 접속이 가능함
    - 거리는 절댓값 핪으로 구한다.
한 BC에 두 명 이상의 사용자가 접속한 경우, 충전 양을 나눈다.

풀이:
사용자의 이동 궤적이 주어짐
1. 이동
2. BC와의 거리 계산(BC 위치 배열)
3. BC 선택에 있어서는 2차원 배열을 인자로 보내준다. 최대 (2 x 8)
    - 가지치기 진행
    BC < 8
- 사용자 좌표는 그냥 업데이트만 시켜준다.
'''

from collections import deque

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]


def bfs(sr, sc, scope, bc):
    visited = [[-1] * 10 for _ in range(10)]
    visited[sr][sc] = 0
    queue = deque([(sr, sc)])
    grid[sr][sc].append(bc)
    while queue:
        r, c = queue.popleft()
        if visited[r][c] >= scope:
            continue
        for d in range(1, len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 10 and 0 <= nc < 10 and visited[nr][nc] == -1:
                grid[nr][nc].append(bc)
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


def charge_bc(person, selected):
    global tmp_charge
    if person == 2:
        tmp_val = 0
        bcs = [0] * (m + 1)
        for i in range(len(selected)):
            bcs[selected[i]] += 1
        for i in range(len(bcs)):
            if bcs[i]:
                tmp_val += bc_charger[i] // bcs[i] * bcs[i]
        tmp_charge = max(tmp_charge, tmp_val)
        return
    else:
        # 만약 bc가 안닿는 위치라면
        if not bc_list[person]:
            charge_bc(person + 1, selected)
        else:
            for i in range(len(bc_list[person])):
                charge_bc(person + 1, selected + [bc_list[person][i]])


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())     # 이동 시간, bc 개수
    a, b = (0, 0), (9, 9)
    a_dir = [0] + list(map(int, input().split()))
    b_dir = [0] + list(map(int, input().split()))
    grid = [[[] * 10 for _ in range(10)] for _ in range(10)]
    bc_charger = [0]
    for i in range(1, m + 1):
        sr, sc, c, p = map(int, input().split())
        bfs(sc - 1, sr - 1, c, i)
        bc_charger.append(p)

    ans = 0
    for time in range(n + 1):
        # 0. 이동하기
        a_d, b_d = a_dir[time], b_dir[time]
        a = (a[0] + dr[a_d], a[1] + dc[a_d])
        b = (b[0] + dr[b_d], b[1] + dc[b_d])
        people = [a, b]

        # 1. BC가 있는지 확인
        bc_list = [0] * 2
        for i in range(2):
            r, c = people[i]
            if grid[r][c]:
                bc_list[i] = grid[r][c]

        # 2. 중복조합으로 최대 출력 찾기
        tmp_charge = 0
        charge_bc(0, [])
        ans += tmp_charge

    print(f'#{tc} {ans}')