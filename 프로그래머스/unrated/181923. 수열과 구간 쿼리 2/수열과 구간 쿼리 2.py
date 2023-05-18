def solution(arr, queries):
    answer = []
    for query in queries:
        numlist = arr[query[0]:query[1] + 1]
        checkNum = [num for num in numlist if num > query[2]]
        
        num = min(checkNum) if len(checkNum) else -1
        
        answer.append(num)
        
    return answer