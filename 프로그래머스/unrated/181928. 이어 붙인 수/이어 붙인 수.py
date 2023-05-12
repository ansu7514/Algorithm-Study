def solution(num_list):
    odd = ''
    even = ''
    
    for num in num_list:
        if num % 2 == 0:
            odd += str(num)
        else:
            even += str(num)
            
    return sum([int(odd), int(even)])