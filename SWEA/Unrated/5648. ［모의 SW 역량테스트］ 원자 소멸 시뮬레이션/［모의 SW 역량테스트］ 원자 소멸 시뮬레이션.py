'''
원자 소멸 시뮬레이션

1. 원자의 최초 위치 : 2차원 평면
2. 상하좌우 존재
3. 모든 원자는 동일하게 움직인다.
4. 모든 원자들은 동시 이동을 시작함
5. 두 개 이상 원자가 동시에 충돌할 경우, 모두 보유한 에너지를 방출하고 소멸한다.

풀이:
한 칸 씩 이동해야 한다.
이동 중간에 충돌하는 경우도 존재함. (이 경우를 판단해주어야 한다.)
원자들 정보 list 생성

1. 이동해보기
2. 방출하기
3. 다음 이동 전 충돌할 수 있는지 체크해보기
4. 만약 범위를 넘어간다면 소멸된 것으로 판단(영원히 소멸되지 않으므로)
'''

from collections import defaultdict

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def move_atoms():
    global ans
    for i in range(len(atom_list)):
        if not atom_list[i]:
            continue
        r, c, d, k = atom_list[i]
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < 4001 and 0 <= nc < 4001):
            atom_list[i] = 0
        else:
            # 중간에서 만나는 경우 체크
            atom_list[i] = (nr, nc, d, k)
            move_loc[(nr, nc)].append(i)


def destroy_atoms():
    global ans
    for key, value in move_loc.items():
        if len(value) > 1:
            for j in range(len(value)):
                num = value[j]
                _, _, _, k = atom_list[num]
                ans += k
                atom_list[num] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    atom_list = [0]

    for i in range(1, n + 1):
        x, y, d, k = map(int, input().split())
        atom_list.append((2 * (2000 - y - 1000), 2 * (x + 1000), d, k))

    ans = 0
    while True:
        if atom_list.count(0) == n + 1:
            break
        move_loc = defaultdict(list)

        # 1. 원자 이동
        move_atoms()

        # 2. 원자 소멸 체크
        destroy_atoms()

    print(f'#{tc} {ans}')