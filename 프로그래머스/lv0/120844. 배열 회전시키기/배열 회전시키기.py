def solution(numbers, direction):
    if direction == 'right':
        temp = numbers[len(numbers) - 1]
        numbers = numbers[:-1]
        numbers.insert(0, temp)
        
        return numbers
    else:
        temp = numbers[0]
        numbers = numbers[1:]
        numbers.append(temp)

        return numbers