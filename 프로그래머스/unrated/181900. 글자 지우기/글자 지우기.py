def solution(my_string, indices):
    temp = list(my_string)
    answer = ''

    for i in range(len(temp)):
        if i not in indices:
            answer += temp[i]
        
    return answer