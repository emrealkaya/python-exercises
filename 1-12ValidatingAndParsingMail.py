import re

n = int(input())

for _ in range(n):
	a,b = input().split('')
	mail = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', b)
	if mail:
		print(a,b)