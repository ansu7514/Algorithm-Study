import math

def solution(fees, records):
    deTime, deFee, ptTime, ptFee = fees;
    
    recordList = {}
    for record in records:
        time, number, io = record.split(' ')
        
        # 딕셔너리 키 값으로 차넘버 별로 분리
        if int(number) in list(recordList.keys()):
            valList = recordList[int(number)]
            valList.append(time)
            recordList[int(number)] = valList
        else:
            recordList[int(number)] = [time]
            
    answer = []
    for car in list(sorted(recordList.keys())): # 차량 번호가 작은 자동차순으로 정렬
        record = recordList[car]
        
        # 길이가 홀수인 경우 마지막 입차 기록만 빼놓기
        last = record.pop() if len(record) % 2 == 1 else 0
        
        total = 0
        if (len(record)):
            for i in range(0, len(record), 2):
                h1, m1 = [int(r) for r in record[i].split(':')]
                h2, m2 = [int(r) for r in record[i + 1].split(':')]
                
                h = (h2 - h1 if m2 >= m1 else h2 - h1 - 1) * 60
                m = m2 - m1 if m2 >= m1 else m2 + 60 - m1

                total += h + m
        
        if (last != 0):
            h1, m1 = [int(l) for l in last.split(':')]
            h2, m2 = 23, 59
            
            h = (h2 - h1 if m2 >= m1 else h2 - h1 - 1) * 60
            m = m2 - m1 if m2 >= m1 else m2 + 60 - m1
            
            total += h + m

        if total <= deTime:
            answer.append(deFee)
        else:
            answer.append(deFee + (math.ceil((total - deTime) / ptTime) * ptFee))
            
    return answer