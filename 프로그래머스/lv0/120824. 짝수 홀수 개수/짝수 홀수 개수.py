def solution(num_list):
    odd = len([num for num in num_list if num % 2 == 0])
    even = len([num for num in num_list if num % 2 != 0])
    
    return [odd, even]