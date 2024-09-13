'''
퍼즐

풀이:
옮길 수 있는 경우만큼 bfs 진행
- 이전에 왔던 방향에 대해서는 continue 시켜주어 중복 제거
- 지금까지 나왔던 모양에 대해서 가지치기를 진행

배열을 string형태로 받아서 진행
- 가지치기 진행 시 dict으로 찾기
    - r = idx // 3
    - c = idx % 3
'''

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(spuzzle):
    queue = deque()
    queue.append(spuzzle)

    while queue:
        puzzle = queue.popleft()
        cnt = docs[puzzle]

        if puzzle == answer:
            return cnt

        # 1차원 인덱스를 2차원 좌표로 변환
        idx = puzzle.index('0')
        r, c = idx // 3, idx % 3

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                # 변환된 2차원 좌표를 다시 1차원 인덱스로 변환
                nidx = nr * 3 + nc
                
                # 새로운 퍼즐 생성
                new_puzzle_list = list(puzzle)
                new_puzzle_list[nidx], new_puzzle_list[idx] = new_puzzle_list[idx], new_puzzle_list[nidx]
                new_puzzle = "".join(new_puzzle_list)

                # 새로운 퍼즐이 딕셔너리에 존재하는지 확인
                # docs.get(찾고자 하는 키, 키가 없을 때 반환할 값)
                if docs.get(new_puzzle, -1) == -1:
                    docs[new_puzzle] = cnt + 1
                    queue.append(new_puzzle)

    return -1


n = 3
puzzle = ""
for i in range(n):
    tmp = input().split()
    for j in range(3):
        puzzle += tmp[j]
answer = "123456780"

if puzzle == answer:
    print(0)
    exit()

cnt = 0
docs = defaultdict(int)
docs[puzzle] = 0
print(bfs(puzzle))
