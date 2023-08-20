def solution(letter):
    strlist = letter.split(' ')
    
    answer = ''
    for s in strlist:
        if s == '.-': answer += 'a'
        elif s == '-...': answer += 'b'
        elif s == '-.-.': answer += 'c'
        elif s == '-..': answer += 'd'
        elif s == '.': answer += 'e'
        elif s == '..-.': answer += 'f'
        elif s == '--.': answer += 'g'
        elif s == '....': answer += 'h'
        elif s == '..': answer += 'i'
        elif s == '.---': answer += 'j'
        elif s == '-.-': answer += 'k'
        elif s == '.-..': answer += 'l'
        elif s == '--': answer += 'm'
        elif s == '-.': answer += 'n'
        elif s == '---': answer += 'o'
        elif s == '.--.': answer += 'p'
        elif s == '--.-': answer += 'q'
        elif s == '.-.': answer += 'r'
        elif s == '...': answer += 's'
        elif s == '-': answer += 't'
        elif s == '..-': answer += 'u'
        elif s == '...-': answer += 'v'
        elif s == '.--': answer += 'w'
        elif s == '-..-': answer += 'x'
        elif s == '-.--': answer += 'y'
        else: answer += 'z'
        
    
    return answer