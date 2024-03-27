def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    for i in range(0, len(score), m):
        arr = score[i:i+m]
        if len(arr) == m:
            min_score = min(arr)
            answer += min_score * m
    return answer
