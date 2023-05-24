def solution(my_strings, parts):
    answer = []
    for i in range(len(my_strings)):
        strings = list(my_strings[i])
        part = parts[i]
        
        result = strings[part[0]:part[1] + 1]
        answer.append(''.join(result))
    
    return ''.join(answer)