def solution(my_string):
    answer = []
    
    start = 0
    for i in range(len(my_string)):
        answer.append(my_string[start:])
        start += 1
    
    return sorted(answer)