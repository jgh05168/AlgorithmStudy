cnt = 0

# dfs : 재귀로 풀기
def dfs(n, t, idx, val):
    global cnt          
    if idx == len(n) and val == t:      # 모든 숫자들에 대한 연산을 수행 & target과 값이 같을 경우
        cnt += 1
        return
    elif idx == len(n):             # 모든 숫자들에 대해 연산을 수행했을 때
        return

    # 이진 트리처럼 구현된다.
    dfs(n, t, idx + 1, val + n[idx])
    dfs(n, t, idx + 1, val - n[idx])


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt