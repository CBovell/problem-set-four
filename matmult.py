#Venuja Perera
#01/10/2022

def mult_scalar(matrix, scale):
	resMatrix = matrix
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			resMatrix[i][j] *= scale
	return resMatrix

def mult_matrix(a, b):
	if ((len(b) != len(a[0])) or (len(a) == 0) or (len(b) ==0) or (len(a[0])==0) or (len(b[0]) ==0)):
		return None

	resMatrix = []
	for i in range (len(a)):
		resMatrix.append([])

	for i in range(len(b[0])):#For each column in matrix b
		for j in range (len(a)):#For each row in matrix a
			currSum=0
			for k in range (len(a[0])):#For each element in row j
				currSum+=a[j][k]*b[k][i]#Multiply the element in j row of 'a' by the corresponding value in i column of 'b' and add it to currSum
			resMatrix[j].append(currSum)#add currSum to the result Matrix
	return resMatrix
			

def euclidean_dist(a,b):
	if len(a[0]) != len(b[0]):
		return None
	
	sum=0
	for i in range (len(a[0])):
		sum+=(a[0][i]-b[0][i])**2
	return (sum)**(1/2)
