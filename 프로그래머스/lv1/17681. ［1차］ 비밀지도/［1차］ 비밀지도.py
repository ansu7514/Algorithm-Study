def make_map(n, arr):
    binArr = []

    for num in arr:
        bin_nums = list(format(num, 'b'))
        bin_len = len(bin_nums)

        result = ''
        if bin_len < n:
            sub = n - bin_len

            while sub != 0:
                result += '0'
                sub -= 1
        
        for bin_num in bin_nums:
            result += bin_num
        
        binArr.append(result)
    
    return binArr

def solution(n, arr1, arr2):
    map1 = make_map(n, arr1)
    map2 = make_map(n, arr2)

    answer = []
    for i in range(n):
        map1_list = list(map1[i])
        map2_list = list(map2[i])

        map_result = ''
        for j in range(n):
            if map1_list[j] == '1' or map2_list[j] == '1':
                map_result += '#'
            else:
                map_result += ' '

        answer.append(map_result)
    
    return answer