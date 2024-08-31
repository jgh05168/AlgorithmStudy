'''
10836 여왕벌

m x m
애벌레들은  매일 에너지를 모아서 정오에 자라는데, 무시가  가능함
이 과정을 n일동안 반복
크기가 커지는 과정
1. 제일 왼쪽 열, 제일 위쪽 행 애벌레들은 자신이 자라는 정도를 스스로 결정한다.
    - 자라는 정도를 왼쪽 제일 아래 칸부터 위로가면서 읽고, 위에 도착하면 오른쪽으로 가면서 읽는다.
2. 나머지 애벌레들은 자신의 왼, 왼위, 위 애벌레들의 정도를 파악한 후, 그 날 가장 많이 자란 애벌레가 자란 만큼 자란다.

풀이:
N < 1000000
규칙을 찾아서 마지막에 더해주는 방식으로 가야한다.
- 백만번 입력 받아서 배열에 누적한 뒤, 배열 업데이트 해주는 방식
-> 14억 .. 시초
=> 이를 해결하기 위해 구간을 나누어 값 업데이트(0, 1, 2)
'''

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    M, N = map(int, input().split())  # M: 가로와 세로 크기, N: 날짜 수
    larva = [1 for _ in range(2 * M - 1)]  # 애벌레의 크기

    for _ in range(N):
        zero, one, two = map(int, input().split())

        for i in range(zero, zero + one):  # 애벌레 크기 1만큼 증가
            larva[i] += 1

        for i in range(zero + one, zero + one + two):  # 애벌레 크기 2만큼 증가
            larva[i] += 2

    # 제일 왼쪽 열과, 제일 위쪽 행의 애벌레는 입력으로 주어진 만큼 커진다.
    # 나머지 애벌레는 항상 자신의 위쪽 애벌레만큼 크기가 커지게 된다.
    # 따라서 [i][j] (i >= 1, j >= 1) 위치의 애벌레는 항상 [0][j]의 애벌레의 크기와 같다.
    for i in range(M):
        for j in range(M):
            if j == 0:
                print(larva[M - (i + 1)], end=' ')
            else:
                print(larva[M + j - 1], end=' ')
        print()