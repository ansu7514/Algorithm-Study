t = int(input())

for _ in range(t):
  n = int(input())
  note_1 = set(map(int, input().split()))
  
  m = int(input())
  note_2 = list(map(int, input().split()))

  for n2 in note_2:
    if n2 in note_1:
      print(1)
    else:
      print(0)