def solution(arr):
    maxLen = max(len(arr), len(arr[0]))
    answer = [[0] * maxLen for _ in range(maxLen)]
    
    for i in range(len(arr)):
        for j in range((len(arr[i]))):
            answer[i][j] = arr[i][j]
            
    return answer