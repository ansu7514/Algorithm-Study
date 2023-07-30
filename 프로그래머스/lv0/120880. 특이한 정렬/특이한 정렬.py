def solution(numlist, n):
    numlist = sorted(numlist, reverse=True)
    
    nl = []
    for num in numlist:
        nl.append(num - n)
    
    answer = []
    while len(nl) != 0:
        temp = [abs(num) for num in nl]
        minN = min(temp)

        for num in nl:
            if minN == abs(num):
                answer.append(num + n)
                nl.remove(num)
        
    return answer