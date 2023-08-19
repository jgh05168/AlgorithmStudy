k = int(input())

# 투에-모스 문자열을 구현한 뒤 출력하게 되면 메모리 초과 발생

# 점화식을 사용하여 문제 해결(위키 참조)
def recur(x):
    if x == 0:      # 1의 개수가 짝수
        return 0
    elif x == 1:    # 1의 개수가 홀수
        return 1
    elif x % 2 == 0:           # t(2n) = t(n)
        return recur(x // 2)
    else:                       # t(2n + 1) = 1 - t(n)
        return 1 - recur(x // 2)

print(recur(k - 1))