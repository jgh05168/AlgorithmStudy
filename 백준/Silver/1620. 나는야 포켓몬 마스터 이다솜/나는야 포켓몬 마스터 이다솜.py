import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_dict = {}
rev_pocketmon_dict = {}
for i in range(N):
    pocketmon = input().rstrip()
    pocketmon_dict.update({pocketmon: i + 1})
    rev_pocketmon_dict.update({i + 1: pocketmon})


for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(rev_pocketmon_dict[int(question)])
    else:
        print(pocketmon_dict[question])