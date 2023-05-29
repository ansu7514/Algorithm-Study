def solution(num_list):
    even = []
    odd = []
    
    for i in range(len(num_list)):
        if (i + 1) % 2 != 0:
            even.append(num_list[i])
        else:
            odd.append(num_list[i])
            
    return sum(even) if sum(even) > sum(odd) else sum(odd)