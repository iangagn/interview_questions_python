/*	
	Time complexity  : O(n)
	Space complexity : O(1)
*/

def isValidSubsequence(array, sequence):
	
	arr_idx = 0
	seq_idx = 0
	while arr_idx < len(array):
		if array[arr_idx] == sequence[seq_idx]:
			seq_idx += 1
		if seq_idx == len(sequence):
			return True
		arr_idx += 1
		
	return False
