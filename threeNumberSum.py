/*	
	Time complexity  : O(n^3)
	Space complexity : O(n)
*/

def threeNumberSum(array, targetSum):
    
	array.sort()
	N = len(array)
	
	triplets = []
	for i in range(0, N - 2):
		for j in range(i + 1, N - 1):
			for k in range(j + 1, N):
				if array[i] + array[j] + array[k] == targetSum:
					triplets.append([array[i], array[j], array[k]])

	return triplets
