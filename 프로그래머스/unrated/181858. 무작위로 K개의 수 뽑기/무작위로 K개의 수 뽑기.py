def solution(arr, k):
    answer = []
    for num in arr:
        if len(answer) == 0 or not (num in answer):
            answer.append(num)
    
    answer = answer[:k]
    
    if len(answer) < k:
        while len(answer) != k:
            answer.append(-1)
    
    return answer