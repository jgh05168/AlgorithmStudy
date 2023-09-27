'''
두가지 경우를 나누어서 생각해 봐야 한다.

1. 양 끝 모두 이전(다음) 값보다 작은 경우 : 다음(이전) 값이 min보다 큰 지 작은지 판단
    1 4 5 2
2. 둘 중 한 값만 차이가 있는 경우 : 이전(다음) 값보다 min이 큰 지 작은지를 판단
    1 4 2 5 / 4 1 5 2
    1 4 3 4

--------- 실패 -----------
그냥 모든 경우에 대해 다 세보자

만약 stats[start] < stats[end]
start += 1
아니라면
end -= 1

계산
'''

N = int(input())
stats = list(map(int, input().split()))

# 초기 포인터 설정
start, end = 0, N - 1
max_stat = (end - start - 1) * min(stats[start], stats[end])

while start <= end:
    if stats[start] < stats[end]:
        start += 1
    else:
        end -= 1

    max_stat = max(max_stat, (end - start - 1) * min(stats[start], stats[end]))

print(max_stat)