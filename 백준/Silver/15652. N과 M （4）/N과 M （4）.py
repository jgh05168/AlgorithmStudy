
def per(i, selected):
    # 종료 조건 : i 가 순열의 길이와 같아진다면
    if i == M:                  
        print(*selected)
        return

    for j in range(N):
        if selected[i - 1] <= arr[j]:   # 만약 수열에 새로 들어올 값이 이전 값보다 같거나 클경우에만 수열을 생성
            selected[i] = arr[j]            
            per(i + 1, selected)        # 다음 자리를 입력하기 위해 재귀호출
            selected[i] = 0             # 입력했던 자리를 초기화시켜주는 과정

N, M = map(int, input().split())

arr = list(i for i in range(1, N + 1))
permitation =[0] * M        # 들어갈 수 있는 빈 수열의 자리 생성
get_list = []

per(0, permitation)