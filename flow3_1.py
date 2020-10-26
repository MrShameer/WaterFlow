import random
import copy

sz=int(input("Size: "))
if sz<8 or sz>20:
	exit()
print("Enter Starting Point, X and Y ")
x=int(input("X: "))
y=int(input("Y: "))
path,sps=" ",1
ran=[[random.randint(0,9) for i in range(sz)] for j in range(sz)]

for i in ran:
	print(i)
print()

#Same as no.2_1. random path cannot go through the previous spot
def flow2(i,j,mat3,dirs,sm):
	sm+=mat3[i][j]
	mat3[i][j]=path
	if i==sz-1:
		for i in range(len(mat3)):
			for j in mat3[i]:
				print(str(j)+sps*" ",end='')	
			print()
		print("Sum: "+str(sm)+"\n")
		return
	r=0
	if dirs==0:
		if j==0:
			r=1
		else:
			r=random.randint(0,1)
	elif dirs==1:
		if j==sz-1:
			r=1
		else:
			r=random.randint(1,2)
	else:
		if j==0:
			r=random.randint(1,2)
		elif j==sz-1:
			r=random.randint(0,1)
		else:
			r=random.randint(0,2)
			
	if r==0:
		flow2(i,j-1,mat3,0,sm)
	elif r==1:
		flow2(i+1,j,mat3,2,sm)
	elif r==2:
		flow2(i,j+1,mat3,1,sm)

flow2(x,y,ran,1,0)