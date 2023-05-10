def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
    else:
        min = arr[0]
        
        for num in arr:
            if min > num:
                min = num
                
        for num in arr:
            if num != min:
                answer.append(num)
    
    return answer