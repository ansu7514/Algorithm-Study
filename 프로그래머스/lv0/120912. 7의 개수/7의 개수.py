def solution(array):
    answer = 0
    
    for num in array:
        temp = list(map(int, str(num)))

        for n in temp:
            if n == 7:
                answer += 1
    
    return answer