'''
"서로 다른" n개의 자연수의 합이 s

s를 알 때 자연수 N의 최댓값은 ? -> 갖고있는 자연수 개수의 최대

풀이 :
- 그리디
1. 1부터 순서대로 더해간다.
2. 만약 현재 자연수를 초과하면
    - 초과한 값 - s < 현재 값 이라면 현재 개수로 출력
'''

s = int(input())
tmp_sum = 0
cnt = 0
for n in range(1, s):
    tmp_sum += n
    if tmp_sum > s:
        if n > tmp_sum - s:
            break
    cnt += 1
    if tmp_sum == s:
        break


if s == 1:
    print(1)
else:
    print(cnt)