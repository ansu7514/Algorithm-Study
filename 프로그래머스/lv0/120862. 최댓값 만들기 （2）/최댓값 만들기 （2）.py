def solution(numbers):
    numList = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                numList.append(numbers[i] * numbers[j])

    return max(numList)