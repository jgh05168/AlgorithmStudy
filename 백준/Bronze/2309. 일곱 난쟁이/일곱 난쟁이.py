ans = []


def recur(cnt, height, check):
    global ans
    if height < 0 or len(check) > 7:
        return
    elif not height and len(check) != 7:
        return
    else:
        if len(check) == 7 and not height:
            for i in range(7 - 1, -1, -1):
                print(check[i])
            exit()
        else:
            for i in range(cnt, len(arr)):
                check.append(arr[i])
                recur(i + 1, height - arr[i], check)
                check.pop()


arr = [0] * 9
for i in range(9):
    arr[i] = int(input())
arr.sort(reverse=True)
heights = 100

recur(0, heights, [])
