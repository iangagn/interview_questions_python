/*
	Brute force solution that goes through all pairs of numbers.
	
	Time complexity  : O(n^2)
	Space complexity : O(1)
*/

def twoNumberSum(array, targetSum): 
	n = len(array)
	i = 0
	while i < n - 1:
		j = i + 1
		while j < n:
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
			j += 1
		i += 1
	return []
