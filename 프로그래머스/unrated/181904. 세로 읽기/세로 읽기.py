def solution(my_string, m, c):
    temp = []

    for i in range(len(my_string)):
        data = list(my_string)
        if i == 0 or i % m == 0:
            temp.append(data[i:i + m])

    answer = ''
    for data in temp:
        answer += data[c - 1]

    return answer