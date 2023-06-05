def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split(' ')
    answer = [s for s in myStr if len(s)]
    
    return answer if len(answer) else ['EMPTY']