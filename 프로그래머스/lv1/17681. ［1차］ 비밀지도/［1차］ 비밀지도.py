def solution(n, arr1, arr2):
    map1 = [format(arr, 'b') for arr in arr1]
    map2 = [format(arr, 'b') for arr in arr2]
    
    answer = []
    for i in range(0, len(arr1)):
        num1 = list(map1[i] if len(map1[i]) == n else ((n - len(map1[i])) * '0') + (map1[i]))
        num2 = list(map2[i] if len(map2[i]) == n else ((n - len(map2[i])) * '0') + (map2[i]))
        
        answer.append(''.join('#' if num1[j] == '1' or num2[j] == '1' else ' ' for j in range(n)))
        
    return answer