strings = [input() for _ in range(5)]

max_len = len(strings[0])
for i in range(1, len(strings)):
    if max_len < len(strings[i]):
        max_len = len(strings[i])

new_str = []
for col in range(max_len):
    for row in range(len(strings)):
        try:
            new_str.append(strings[row][col])
        except:
            continue

print(''.join(new_str))