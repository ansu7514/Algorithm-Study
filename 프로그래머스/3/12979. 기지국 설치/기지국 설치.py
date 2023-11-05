import math

def solution(n, stations, w):
    stationRange = w * 2 + 1
    answer = 0
    start = 1

    for s in stations:
        end = s - w

        if end < 2:
            start = s + w + 1
        else:
            station = end-start
            answer += math.ceil(station/stationRange)
            start = s + w + 1
            
    if s + w  < n:
        start = s + w
        station = n - start
        answer += math.ceil(station/stationRange)

    return answer