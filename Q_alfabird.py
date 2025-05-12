for i in range (7):
	for j in range (6):
		if i==0 and j<5:
			print("*",end=" ")
		elif j==0 and i<6:
			print("*",end=" ")
		elif i==5 and j<5:
			print("*",end=" ")
		elif j==4 and i<6:
			print("*",end=" ")
		elif i==1 and i==6:
			print("*",end=" ")
		elif i-j==1 and j>1:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print( )