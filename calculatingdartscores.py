a = ["", "single", "double", "triple"]
n = int(input())
for i in range(1,21):
	for j in range(1,21):
		for k in range(1,21):
			for x in range(4):
				for y in range(4):
					for z in range(4):
						if n == i*x + j*y + k*z:
							if x > 0:
								print(a[x] + " " + str(i))
							if y > 0:
								print(a[y] + " " + str(j))
							if z > 0:
								print(a[z] + " " + str(k))
							quit()
print("impossible")