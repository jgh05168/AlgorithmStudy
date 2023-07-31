
def solution(progresses, speeds):
    day = 0
    fin_info = []
    while len(progresses) :
        if progresses[0] >= 100:
            fin_info.append(str(day))
            progresses.pop(0)
            speeds.pop(0)
        else:
            for idx in range(0, len(progresses)):
                progresses[idx] += speeds[idx]
            day += 1

    output = {}
    for info in fin_info:
        if str(info) in output.keys():
            output.update({info : output.get(info) + 1})
        else:
            output.update({info: 1})
            
    return list(output.values())

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))