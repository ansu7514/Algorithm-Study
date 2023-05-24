def solution(a, b, c, d):
    numlist = [a, b, c, d]
    count = {}

    for i in numlist:
        try: count[i] += 1
        except: count[i] = 1
    
    if len(count) == 1:
        return 1111 * a
    elif len(count) == 3:
        sum = 1
        for key in count:
            if count[key] != 2:
                sum *= key
        return sum
    elif len(count) == 4:
        return min(numlist)
    else:
        key_list = list(count.keys())
        value_list = list(count.values())
        
        if 2 in value_list:
            p = key_list[0]
            q = key_list[1]
            return (p + q) * abs(p - q)
        else:
            if value_list[0] == 3:
                p = key_list[0]
                q = key_list[1]
            else:
                p = key_list[1]
                q = key_list[0]
            return (10 * p + q) ** 2