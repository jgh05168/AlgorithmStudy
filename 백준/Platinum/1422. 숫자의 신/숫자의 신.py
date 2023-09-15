'''
1. 갖고 있는 숫자들을 적어도 한 번은 사용해야 되므로 일단 list에 넣어두고 시작

2. 갖고있는 수들은 중복이 가능하므로 남은 자리를 갖고있는 수들 중 가장 큰 수로 채워넣기

3. 문자열을 사전순으로 정렬하기 - 단순 정렬이 아니라 각 수는 1000000000(10**9)보다 작거나 같으므로,
    최소값인 문자열 * 10을 한 값에 대해서 사전순으로 내림차순 정렬
    --> 숫자를 조합해서 최대값을 찾는 문제는 이 방법을 적극 활용하자

4. 정렬된 list값 이어붙이기

'''

from collections import deque
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
num_list = []

# 적어도 한 번씩 사용되기 위한 숫자를 리스트에 넣어준다.
max_num = '0'
for i in range(K):
    number = input().rstrip()
    num_list.append(number)
    if int(max_num) < int(number):      # 최대값 찾아주기
        max_num = number

# 남은 자리에 최대값 넣어주기
for i in range(N - K):
    num_list.append(max_num)

# 문자열을 사전순으로 정렬(각 수들을 10**10 이상으로 만들어준 뒤 정렬)
# 숫자문자열의 경우 앞자리부터 순차적으로 사전순으로 비교하게 된다.
# 만약 숫자가 모두 같을 경우 문자열의 길이가 더 긴 것이 더 큰 값이 된다.
num_list.sort(key=lambda x: x*10, reverse=True)     # 문자열이므로 *10하는 것이 제곱과 다름없다.
ans = ''.join(num_list)

print(ans)