for i in range (6):
	for j in range (4):
		if i==0 or j==0 or i==2 or i==1 and j==3 or i-j==2 :
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print( )	