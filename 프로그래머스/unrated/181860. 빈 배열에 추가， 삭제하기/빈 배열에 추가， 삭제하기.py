def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i]:
            answer += [arr[i] for num in range(arr[i] * 2)]
        else:
            for num in range(arr[i]):
                answer.pop()
            
    return answer