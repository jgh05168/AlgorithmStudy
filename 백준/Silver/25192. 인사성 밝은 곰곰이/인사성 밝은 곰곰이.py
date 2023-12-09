import sys
input = sys.stdin.readline

n = int(input())
gomgom = 0
user_dict = {}
for _ in range(n):
    chat = input().rstrip()
    if chat == 'ENTER':
        user_dict.clear()
    else:
        try:
            if user_dict[chat]:
                continue
        except:
            user_dict.update({chat: 1})
            gomgom += 1

print(gomgom)