def solution(participant, completion):
    length = len(participant)
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if(completion[i] != participant[i]):
            return participant[i]
        
    return participant[len(completion)]
        