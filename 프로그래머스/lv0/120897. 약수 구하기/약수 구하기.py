def solution(n):
    return [num for num in range(n + 1) if num != 0 and n % num == 0]