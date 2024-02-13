def solution(x):
    li = list(map(int,str(x)))
    answer = True if x % sum(li) == 0 else False
    return answer