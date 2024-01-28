t = int(input())

for _ in range(t):
	n = int(input())
	nList = set(map(int, input().split()))

	m = int(input())
	mList = list(map(int, input().split()))

	for num in mList:
		if num in nList:
			print(1)
		else:
			print(0)