def solution(num_list):
    num1 = num_list[len(num_list) - 1]
    num2 = num_list[len(num_list) - 2]
    
    num_list.append(num1 - num2 if num1 > num2 else num1 * 2)
    return num_list