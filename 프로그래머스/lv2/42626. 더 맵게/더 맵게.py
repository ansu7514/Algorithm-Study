from heapq import heappush, heappop
    
def solution(scoville, K):
    answer = 0
    heap = []
    
    for num in scoville:
        heappush(heap, num)

    minNum = heap[0]
    while minNum < K and len(heap) != 1:
        first = heappop(heap)
        second = heappop(heap)
        mix = first + (second * 2)
        heappush(heap, mix)

        minNum = heap[0]
        answer += 1

    return -1 if len(heap) == 1 and heap[0] < K else answer