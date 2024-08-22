'''
단어 수학
알파벳 대문자를 0 ~ 9로 바꿔서 n개의 수를 합하는 문제

알파벳의 수는 겹쳐서는 안된다.

두 수의 합 중 최대를 구하자

풀이 :
비교해야 할 값 :
1. 자리수
2. 빈도

만약 자리수가 같다면 ? 앞쪽에 더 많이 나온 빈도수를 체크해야 한다.
자리수 * 10 을 하여 개수 정보를 세어 준다.
그 다음 정렬ㅏ고, 순차적으로 값을 매겨 준다.
'''

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
alphabet_list = [list(input().rstrip()) for _ in range(n)]
alpha_dict = defaultdict(int)
for i in range(n):
    m = len(alphabet_list[i]) - 1
    for j in range(1, len(alphabet_list[i]) + 1):
        alpha_dict[alphabet_list[i][j - 1]] += 10**m
        m -= 1

alpha_dict = dict(sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True))

alpha_to_val = defaultdict(int)
value = 9
for key in alpha_dict.keys():
    if not alpha_to_val[key]:
        alpha_to_val[key] = value
        value -= 1

ans = 0
for i in range(n):
    m = len(alphabet_list[i]) - 1
    for j in range(len(alphabet_list[i])):
        ans += alpha_to_val[alphabet_list[i][j]] * (10 ** m)
        m -= 1

print(ans)