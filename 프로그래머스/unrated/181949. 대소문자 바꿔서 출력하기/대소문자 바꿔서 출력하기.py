str = input()

answer = ''

for s in list(str):
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()

print(answer)