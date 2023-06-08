def solution(arr):
    stk = []

    for i in range(len(arr)):
        if (stk == []):
            stk.append(arr[i])
        elif (arr[i] == stk[-1]):
            stk.pop()
        else:
            stk.append(arr[i])

    return stk if len(stk) else [-1]