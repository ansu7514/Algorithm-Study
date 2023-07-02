a, b, v = input().split(' ')
a, b, v = int(a), int(b), int(v)

day = (v - b) // (a - b)

if (v - b) % (a - b) != 0:
    day += 1

print(day)