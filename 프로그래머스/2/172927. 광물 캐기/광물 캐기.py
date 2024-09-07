'''
광물캐기. 피로도 소모가 존재함
- 사용할 수 있는 곡괭이 중 아무거나 사용
- 한 번 사용하기 시작한 곡괭이는 계속 사용
- 광물의 순서는 변경 불가능
- 모든 광물을 캐거나, 곡괭이가 없을 때 까지 진행
- 각 곡괭이는 광물 5개를 캐면 부러진다.

최소한의 피로도를 반환

'''

import sys, heapq
input = sys.stdin.readline

def solution(picks, minerals):
    answer = 0
    mineral_grid = []
    tmp = []
    for i in range(len(minerals)):
        if not i % 5:
            mineral_grid.append(tmp)
            tmp = []
        tmp.append(minerals[i])
    if tmp:
        mineral_grid.append(tmp)

    # 점수 계산 시작
    pq = []
    for i in range(1, min(sum(picks) + 1, len(mineral_grid))):
        total, dia, iron, stone = 0, 0, 0, 0
        for j in range(len(mineral_grid[i])):
            if mineral_grid[i][j] == 'diamond':
                total += 25
                dia += 1
            elif mineral_grid[i][j] == 'iron':
                total += 5
                iron += 1
            else:
                stone += 1
        heapq.heappush(pq, (-total, -dia, -iron, -stone))

    # 우선순위큐에서 출력하며 높은 곡괭이 사용하기
    idx = 0
    for i in range(len(picks)):
        if picks[i]:
            idx = i
            break
    while idx <= 2 and pq:
        _, dia, iron, stone = heapq.heappop(pq)
        dia *= -1
        iron *= -1
        stone *= -1
        if not idx:
            answer += dia + iron + stone
        elif idx == 1:
            answer += dia * 5 + iron + stone
        else:
            answer += dia * 25 + iron * 5 + stone


        # 곡괭이 다 썼으면 하나 늘리기
        picks[idx] -= 1
        if not picks[idx]:
            while idx <= 2 and not picks[idx]:
                idx += 1

    return answer