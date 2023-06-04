def solution(binomial):
    a, op, b = binomial.split(' ')

    answer = 0
    if op == '+':
        answer = int(a) + int(b)
    elif op == '-':
        answer = int(a) - int(b)
    elif op == '*':
        answer = int(a) * int(b)
    else:
        answer = int(a) // int(b)

    return answer