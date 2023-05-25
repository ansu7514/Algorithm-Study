def solution(s):
    temp = list(s)

    check = 0
    for i in range(len(temp)):
        if temp[i] == '(':
            check += 1
        else:
            check -= 1

        if check < 0:
            return False

    return True if check == 0 else False