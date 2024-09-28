'''
n개의 스위치, n개의 전구
i번 스위치를 누르면 i - 1, i + 1, i 세 개의 상태가 바뀐다.

현재 스위치와 결과 자리수가 같은 경우 : 다음 결과가 다르다면, 누르기
현재 스위치와 결과 자리수가 다른 경우 : 이전 애들이 다르면 누르기
'''
import copy
import sys
input = sys.stdin.readline

def push(switch, cnt):
    for i in range(1, n - 1):
        # 0. 만약 세군대 모두
        # 1. 이전 애들부터 신경쓰기
        if switch[i - 1] != target[i - 1]:
            cnt += 1
            switch[i - 1] = not switch[i - 1]
            switch[i] = not switch[i]
            switch[i + 1] = not switch[i + 1]

        # 2. 다음 애들 신경쓰기
        elif switch[i] == target[i] and switch[i - 1] != target[i - 1]:
            if switch[i + 1] != target[i + 1]:
                cnt += 1
                switch[i - 1] = not switch[i - 1]
                switch[i] = not switch[i]
                switch[i + 1] = not switch[i + 1]

        # 맞는지 체크
        if switch == target:
            return cnt

    # 맨 마지막 놈
    if switch[-1] != target[-1]:
        cnt += 1
        switch[-2] = not switch[-2]
        switch[-1] = not switch[-1]

    if switch == target:
        return cnt
    return 0

n = int(input())
switch_off = list(int(i) == 1 for i in input().rstrip())
# 맨 처음 놈은 누르는지, 누르지 않는지 모든 경우에 대해 판단
switch_on = copy.deepcopy(switch_off)
switch_on[0] = not switch_on[0]
switch_on[1] = not switch_on[1]

target = list(int(i) == 1 for i in input().rstrip())

# 바로 끝나는 경우
if switch_off == target:
    print(0)
elif switch_on == target:
    print(1)
else:
    # 스위치 안 누른 애부터 시작
    cnt = push(switch_off, 0)
    if cnt:
        print(cnt)
    else:
        cnt = push(switch_on, 1)
        if cnt:
            print(cnt)
        else:
            print(-1)
