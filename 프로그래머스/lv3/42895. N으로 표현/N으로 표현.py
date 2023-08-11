def recur(N, number, val, cnt):
    global ans
    if cnt > 8:
        return
    if val == number:
        if ans > cnt or ans <= 0:
            ans = cnt
        return

    # N을 1 ~ 8개 사용하는 경우를 각각 생각해준다. -> 최대 8번 연산됌
    new_val = 0
    for i in range(1, 9):
        new_val = new_val * 10 + N      # N을 1 ~ 8번 이어붙이는 경우에 대해 고려
        recur(N, number, val + new_val, cnt + i)
        recur(N, number, val - new_val, cnt + i)
        recur(N, number, val * new_val, cnt + i)
        recur(N, number, val // new_val, cnt + i)

def solution(N, number):
    global ans
    ans = -1
    recur(N, number, 0, 0)
    return ans

