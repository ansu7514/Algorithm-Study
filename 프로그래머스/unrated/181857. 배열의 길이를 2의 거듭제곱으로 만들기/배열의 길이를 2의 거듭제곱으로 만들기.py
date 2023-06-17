def solution(arr):
    num = 1

    while num < len(arr):
        num *= 2
    
    answer = []
    for i in range(num):
        if i < len(arr):
            answer.append(arr[i])
        else:
            answer.append(0)

    return answer