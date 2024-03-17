import math
def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):
        remains = 100 - progress
        days.append(math.ceil(remains/speed))
    
    index = 0
    for i in range(len(days)):
        if days[index] < days[i]:
            answer.append(i - index)
            index = i
    answer.append(len(days) - index)
    return answer