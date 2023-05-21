def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
        elif stk[-1] >= arr[i]:
            stk.pop()
            i -= 1
        i += 1
        
    return stk