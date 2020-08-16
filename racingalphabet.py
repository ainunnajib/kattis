from math import *
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
t = pi/7.0
n = int(input())
for i in range(n):
	s = input()
	position = a.index(s[0])
	time = 0.0
	for j in range(len(s)):
		nextstep = a.index(s[j])
		dist = min((28+nextstep-position)%28, (28+position-nextstep)%28)*t
		time += (dist+1)
		position = nextstep
	print(time)