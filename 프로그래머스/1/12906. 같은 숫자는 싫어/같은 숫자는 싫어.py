def solution(arr):
    answer = []
    for i in arr:
        length = len(answer)
        if length == 0 or (length>= 1 and answer[length-1] != i):
            answer.append(i)
    return answer