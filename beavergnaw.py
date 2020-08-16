from math import *
l = input().split()
while l[0] != "0":
	D = float(l[0])
	V = float(l[1])
	result = (D**3 - V*6/pi)**(1./3.)
	print(result)
	l = input().split()