def solution(arr):
    check = [i for i in range(len(arr)) if arr[i] == 2]
    
    answer = []
    if len(check):
        start = check[0]
        end = check[-1] + 1
        return arr[start:end]
    else:
        return [-1]