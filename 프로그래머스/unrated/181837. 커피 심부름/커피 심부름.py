def solution(order):
    answer = 0
    for bev in order:
        if 'cafelatte' in bev:
            answer += 5000
        else:
            answer += 4500

    return answer