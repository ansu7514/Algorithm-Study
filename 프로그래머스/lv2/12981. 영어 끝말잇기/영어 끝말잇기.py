def solution(n, words):
    person, turn = 0, 0
    
    past = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in past and past[-1][-1] == words[i][0]:
            past.append(words[i])       
        else:
            turn = (i + 1) // n + 1 if (i + 1) % n != 0 else (i + 1) // n
            person = (i % n) + 1
            break

    return person, turn