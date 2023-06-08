def solution(myString, pat):
    myString = myString.replace('A', 'b').replace('B', 'a').upper()
    
    return 1 if pat in myString else 0