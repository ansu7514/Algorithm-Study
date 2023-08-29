def solution(my_string):
    answer = 0
    check = 0
    
    for n in my_string.split(' '):
        if n == '+':
            check = 1
        elif n == '-':
            check = 2
        else:
            if check == 1:
                answer += int(n)
            elif check == 2:
                answer -= int(n)
            else:
                answer = int(n)
    
    return answer