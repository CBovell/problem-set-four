def mult_scalar(matrix, scale):
	resMatrix = matrix
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			resMatrix[i][j] *= scale
	return resMatrix

def mult_matrix(a, b):
	return [[]]
	
def euclidean_dist(a,b):
	return -1