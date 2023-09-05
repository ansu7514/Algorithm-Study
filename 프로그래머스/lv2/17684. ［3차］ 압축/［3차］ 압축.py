def solution(msg):
    answer = []
    
    # index 목록
    index = {}
    for n in range(65, 91):
        index[chr(n)] =  int(n - 64)
    
    idx, w = 0, ''
    while idx < len(msg):
        w += msg[idx]
        
        # 글자가 있을 경우
        if w in index.keys():
            idx += 1
            continue
        # 글자가 없을 경우
        else:
            index[w] = len(index) + 1
            
            check = w[:-1]
            answer.append(index[check])
            w = ''
    
    # 마지막 글자 추가
    answer.append(index[w])
        
    return answer