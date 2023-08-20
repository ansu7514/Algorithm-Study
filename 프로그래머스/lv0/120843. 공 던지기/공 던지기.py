def solution(numbers, k):
    idx = 0
    while k != 1:
        idx += 2
        
        if idx > len(numbers) - 1:
            idx = idx % len(numbers)
            
        k -= 1
    
    return numbers[idx]