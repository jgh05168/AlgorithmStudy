'''

풀이 : 서로 자리수를 확인해가며 모두 다른 경우가 존재한다면 break
2 <= n <= 1000 n2까지 충분히 ㄱㄴ
'''

import sys
input = sys.stdin.readline

n = int(input())
std_nums = [[] * 100 for _ in range(100)]
for _ in range(n):
    std_num = input().rstrip()
    # 값을 뒤에서부터 잘라서 미리 저장시켜보기
    for i in range(len(std_num)):
        std_nums[i].append(std_num[len(std_num) - i - 1:])

# 최대 k만큼 확인해보기 - set 사용하여 중복 제거하고 n과 개수 일치하는지 확인
for k in range(101):
    tmp_nums = set(std_nums[k])
    if n == len(tmp_nums):
        print(k + 1)
        break