def solution(num_list):
    count = 0
    
    for num in num_list:
        temp = num
        while temp != 1:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = (temp - 1) // 2
            
            count += 1
    
    return count