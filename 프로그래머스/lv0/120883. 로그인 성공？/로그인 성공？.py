def solution(id_pw, db):
    lgId, lgPw = id_pw

    answer = 'fail'
    for ID, PW in db:
        if ID == lgId and PW == lgPw:
            answer = 'login'
        elif ID == lgId and PW != lgPw:
            answer = 'wrong pw'
    
    return answer