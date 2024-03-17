def solution(citations):
    answer = 0
    for h in range(max(citations),0,-1):
        count = 0
        for cita in citations:
            if h <= cita:
                count += 1
        if count >= h:
            return h
    return 0