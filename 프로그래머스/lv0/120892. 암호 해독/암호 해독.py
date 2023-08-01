def solution(cipher, code):
    ciph = list(cipher)
    
    answer = ''
    for i in range(len(ciph)):
        if (i + 1) % code == 0:
            answer += ciph[i]

    return answer        