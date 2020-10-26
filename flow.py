import random
import copy

sz=int(input("Size: "))
if sz<8 or sz>20:
	exit()
path,sp=" ",1
ran=[[random.randint(0,9) for i in range(sz)] for j in range(sz)]

def flow(i,j,flw,sm):
	sm+=flw[i][j]
	flw[i][j]=path
	if i==sz-1 or j==sz-1:
		for i in range(len(flw)):
			for j in flw[i]:
				print(str(j)+sp*" ",end='')	
			print()
		print("Sum: "+str(sm)+"\n")
		return
	if flw[i+1][j]>flw[i][j+1]:
		flow(i,j+1,flw,sm)
	elif flw[i+1][j]<flw[i][j+1]:
		flow(i+1,j,flw,sm)
	else:
		flow(i,j+1,copy.deepcopy(flw),copy.deepcopy(sm))
		flow(i+1,j,copy.deepcopy(flw),copy.deepcopy(sm))
for i in ran:
	print(i)
print()
flow(0,0,ran,0)
