import sys,os
import time
os.system("")

rows,cols = (31,31)
grid = [[" "]*rows for i in range(cols)] # grid 

def transpose_grid(_2Dlist_):
	transposed_list = list(zip(*_2Dlist_)) # transpose the grid
	return transposed_list

def list_matric_print(_2Dlist_):
	for i in range(rows):
		for j in range(cols):
			x = '\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in _2Dlist_])
	print(x)
	print("\n"*10)
	
#-------------------------Drawing the pattern ( Right )---------
	#center line
for i in range (15,16) :
	for j in range(15,31) :
			grid[i][j]="*"
	#upper triangle
for i in range (12,15) :
	x=i-11
	for j in range(28,x+28) :
		 grid[i][j-1]="*"
		 
	#lower Triangle
for i in range (16,19) :
	x = 18-i
	for j in range(28+x,27,-1):
			grid[i][j-1]="*" 
#---------------------------------------------------------------

while True :
	#os.system('cls')
	grid=transpose_grid(grid)
	list_matric_print(grid)
	grid = grid[::-1]
	#print("\n")
	#time.sleep(0.1)
	
	
