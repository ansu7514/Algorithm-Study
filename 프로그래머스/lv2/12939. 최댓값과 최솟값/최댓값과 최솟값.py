def solution(s):
    numList = [int(num) for num in s.split(' ')]
    
    min = numList[0]
    max = numList[0]
    
    for num in numList:
        if num < min:
            min = num
        elif num > max:
            max = num

    return f'{min} {max}'