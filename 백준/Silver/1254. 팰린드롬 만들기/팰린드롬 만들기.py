'''
슬라이싱 윈도우 사용하자

for 문 돌면서 절반을 찾는다.
(절반, 절반을 역으로 했을 때)   가 같은 부분 + 더 긴 쪽 만큼 더해주기
'''

import sys
s = sys.stdin.readline().strip()

for i in range(len(s)):
  if s[i:] == s[i:][::-1]:
    print(len(s)+i)
    break