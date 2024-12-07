'''
문자열을 주면 그 중 최대 n개 종류의 알파벳을 가진 연속된 문자열밖에 인식하지 못함

인식할 수 있는 최대 문자열의 길이는 얼마일까?

- 문자열 정렬하면 안된다.
- 투포인터로 시작 위치, 새로 들어오는 위치에 대해 기억해야 한다.
- 문자열이 n개만큼 입력되어 있고, 새로운 문자가 들어온다면
    -> 한 문자가 모두 빠질 때까지 시작 인덱스를 땡겨준다.
'''

from collections import defaultdict

n = int(input())
s = input()

start, end = 0, 0
ans, cnt = 0, 0
alphabet = defaultdict(int)
for idx in range(len(s)):
    if alphabet[s[idx]]:
        alphabet[s[idx]] += 1
    else:
        # n개를 넘어설 때, ans 업데이트 후 조정해주기
        if cnt == n:
            ans = max(ans, end - start + 1)
            while start < end:
                alphabet[s[start]] -= 1
                start += 1
                if not alphabet[s[start - 1]]:
                    break
            cnt -= 1
        alphabet[s[idx]] += 1
        cnt += 1
    end = idx

ans = max(ans, end - start + 1)

print(ans)