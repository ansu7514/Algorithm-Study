def solution(s):
    numList = [int(num) for num in s.split(' ')]
    numList.sort()
    
    return f'{numList[0]} {numList[-1]}'