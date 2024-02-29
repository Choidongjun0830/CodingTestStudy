def solution(clothes):
    answer = 1
    arr = {}
    for clo in clothes:
        name, category = clo[0], clo[1]
        if category not in arr:
            #name을 list
            arr[category] = [name]  
        else:
            arr[category].append(name)
    for v in arr.values():
        answer *= (len(v)+1)
    return answer - 1 