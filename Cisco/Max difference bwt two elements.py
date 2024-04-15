# Largest value appears after the smaller number 


def funcMaxDifference(inputArr):
	# Write your code here
	min_num = inputArr[0]
	max_diff = 0
	for i in range(1, len(inputArr)):
		if(inputArr[i]< min_num):
			min_num = inputArr[i]
		elif inputArr[i] - min_num> max_diff:
			max_diff = inputArr[i] - min_num	
	return max_diff


print(funcMaxDifference([2,3,10,6,4,8,1]))