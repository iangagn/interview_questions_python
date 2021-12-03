/*
	Solution based on a set whose find operation is O(1) via hashing.
	
	Time complexity  : O(n) -> for val in array
	Space complexity : O(n) -> seen_values
*/

def firstDuplicateValue(array):
	
	seen_values = set()
	for val in array:
		if val in seen_values:
			return val
		seen_values.add(val)
	return -1
