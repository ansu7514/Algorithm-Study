def solution(n):
    answer, temp = [], []
    
    for i in range(n):
        temp.append(0)
    
    for i in range(n):
        insert = temp[:]
        insert[i] = 1
        answer.append(insert)
    
    return answer