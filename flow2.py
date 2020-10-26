import random
import copy

sz=int(input("Size: "))
if sz<8 or sz>20:
	exit()
ran=[[]]
path,sp=" ",1
ran=[[random.randint(0,9) for i in range(sz)] for j in range(sz)]

#random path that can go through the previous spot
def flow2(i,j,flw,sm):
	sm+=flw[i][j]
	flw[i][j]=99
	if i==sz-1:
		for i in range(len(flw)):
			for j in flw[i]:
				if j==99:
					j=path
				print(str(j)+sp*" ",end='')	
			print()
		print("Sum: "+str(sm)+"\n")
		return

	if j==0:
		if flw[i+1][j]>flw[i][j+1]:
			flow2(i,j+1,flw,sm)
		elif flw[i+1][j]<flw[i][j+1]:
			flow2(i+1,j,flw,sm)
		else:
			flow2(i,j+1,copy.deepcopy(flw),copy.deepcopy(sm))
			flow2(i+1,j,copy.deepcopy(flw),copy.deepcopy(sm))
	elif j==sz-1:
		if flw[i+1][j]>flw[i][j-1]:
			flow2(i,j-1,flw,sm)
		elif flw[i+1][j]<flw[i][j-1]:
			flow2(i+1,j,flw,sm)
		else:
			flow2(i,j-1,copy.deepcopy(flw),copy.deepcopy(sm))
			flow2(i+1,j,copy.deepcopy(flw),copy.deepcopy(sm))
	else:
		if flw[i][j-1]<flw[i+1][j] and flw[i][j-1]<flw[i][j+1]:
			flow2(i,j-1,flw,sm)
		elif flw[i+1][j]<flw[i][j-1] and flw[i+1][j]<flw[i][j+1]:
			flow2(i+1,j,flw,sm)
		elif flw[i][j+1]<flw[i][j-1] and flw[i][j+1]<flw[i+1][j]:
			flow2(i,j+1,flw,sm)
		else:
			if flw[i][j-1]==flw[i+1][j] and flw[i][j-1]==flw[i][j+1]:
				flow2(i,j-1,copy.deepcopy(flw),copy.deepcopy(sm))
				flow2(i+1,j,copy.deepcopy(flw),copy.deepcopy(sm))
				flow2(i,j+1,copy.deepcopy(flw),copy.deepcopy(sm))
			elif flw[i][j-1]==flw[i+1][j]:
				flow2(i,j-1,copy.deepcopy(flw),copy.deepcopy(sm))
				flow2(i+1,j,copy.deepcopy(flw),copy.deepcopy(sm))
			elif flw[i][j-1]==flw[i][j+1]:
				flow2(i,j-1,copy.deepcopy(flw),copy.deepcopy(sm))
				flow2(i,j+1,copy.deepcopy(flw),copy.deepcopy(sm))
			elif flw[i+1][j]==flw[i][j+1]:
				flow2(i+1,j,copy.deepcopy(flw),copy.deepcopy(sm))
				flow2(i,j+1,copy.deepcopy(flw),copy.deepcopy(sm))
	

for i in ran:
	print(i)
print()
flow2(0,0,ran,0)