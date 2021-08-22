# Question no.02
# find the first Equilibium Point 
def equilibrium(arr):
	leftsum = 0
	rightsum = 0
	n = len(arr)
	for i in range(n):
		leftsum = 0
		rightsum = 0
	
		# for left sum      
		for j in range(i):
			leftsum += arr[j]
		
		# for right sum
		for j in range(i + 1, n):
			rightsum += arr[j]
		
		# if leftsum and rightsum are same,
		if leftsum == rightsum:
			return i
	return -1	
arr = [1,3,5,2,2]
print ("This is the equilibrium ponit Number",equilibrium(arr))


