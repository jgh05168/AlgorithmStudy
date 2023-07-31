import copy

def carry(weight):
    sandbags = []
    optimal_sandbags = []

    for i in range(0, weight // 3):
        sandbags.append(3)

    try:
        for i in range(0, len(sandbags)):
            total_weight = sum(sandbags)

            if total_weight > weight:
                sandbags.pop(-1)
                total_weight = sum(sandbags)

            if total_weight - weight == 0 :
                optimal_sandbags = copy.deepcopy(sandbags)

            sandbags[i] = 5

        return optimal_sandbags
    
    except:
        return optimal_sandbags


N = int(input())


if N < 3 or N > 50000:
    quit()

if N == 3 or N == 5:
    print(1)
elif carry(N) == []:
    print(-1)
else:
    print(len(carry(N)))