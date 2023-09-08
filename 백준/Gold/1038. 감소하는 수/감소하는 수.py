N = int(input())

# 해당 배열이 감소하는 수 인지 확인
def check(i):
    global num
    if len(num) == 1 or num[-2] > i:
        return 1
    else:
        return 0

num = []        # 숫자를 만들어주기 위한 배열
ans = []        # 가능한 x값들을 저장하기 위한 배열

def dfs(depth):
    global num
    for i in range(10):
        num.append(i)
        if check(i):
            dfs(depth + 1)      
            # 자릿수가 이전 자리수보다 같거나 크다면 재귀를 빠져나온 뒤 ans에 현재 num을 문자열로 변환한 뒤 저장
            ans.append(int(''.join(str(x) for x in num)))
        num.pop()


dfs(0)
ans.sort()

# 감소하는 수는 1022개 존재 그외는 -1 출력
if N >= len(ans):
    print(-1)
else:
    print(ans[N])