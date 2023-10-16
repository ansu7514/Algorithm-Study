import heapq

def solution(n, works):
    worklist = []
    for w in works:
        heapq.heappush(worklist, -w)
        
    while n > 0:
        maxtime = heapq.heappop(worklist)
        heapq.heappush(worklist, (maxtime + 1))
        n -= 1
        
    checkTrue = False
    for w in worklist:
        if w > 0: checkTrue = True
    
    if checkTrue:
        return 0
    else:
        answer = 0
        for w in worklist:
            answer += w ** 2
            
        return answer