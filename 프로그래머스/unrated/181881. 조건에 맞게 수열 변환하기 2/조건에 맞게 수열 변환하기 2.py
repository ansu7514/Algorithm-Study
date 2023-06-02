def solution(arr):
    answer = 0
    count = 0

    beforArr = arr[:]
    while count != len(arr):
        count = 0
        beforArr = arr[:]

        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] //= 2
            elif arr[i] % 2 != 0 and arr[i] < 50:
                arr[i] = arr[i] * 2 + 1

            if arr[i] == beforArr[i]:
                count += 1

        answer += 1

    return answer - 1