def solution(s):
    numlist = s.split(' ')
    
    arr = []
    for num in numlist:
        if num != 'Z':
            arr.append(int(num))
        else:
            arr.pop()
            
    return sum(arr)