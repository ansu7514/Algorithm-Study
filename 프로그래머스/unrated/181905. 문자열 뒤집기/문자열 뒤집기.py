def solution(my_string, s, e):
    temp = list(my_string)
    change = temp[s:e + 1]
    change.reverse()

    answer = temp[:s] + change + temp[e + 1:]
    
    return ''.join(answer)