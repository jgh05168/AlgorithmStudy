def enqueue(item):
    global rear
    rear = (rear + 1) % n
    numbers[rear] = item

def dequeue():
    global front
    front = (front + 1) % n
    val = numbers[front]
    numbers[front] = -1
    return val


for i in range(1, 11):
    tc = int(input())
    numbers = [-1] + list(map(int, input().split()))
    n = len(numbers)
    front, rear = 0, n - 1

    cnt = 1
    while 1:

        if cnt == 6:
            cnt = 1
        item = dequeue()
        item -= cnt
        if item <= 0:
            item = 0
            enqueue(item)
            break
        cnt += 1
        enqueue(item)


    while numbers[-1] != 0:
        item = dequeue()
        enqueue(item)

    print(f'#{tc}', end=' ')
    print(*numbers[1:])
