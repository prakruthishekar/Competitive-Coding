# # Maximum value of arr[j] - arr[i] such that j > i

# # Naive

# # Python 3 code to find Maximum difference
# # between two elements such that larger
# # element appears after the smaller number

# # The function assumes that there are at
# # least two elements in array. The function
# # returns a negative value if the array is
# # sorted in decreasing order. Returns 0
# # if elements are equal


# def maxDiff(arr, arr_size):
# 	max_diff = arr[1] - arr[0]
	
# 	for i in range( 0, arr_size ):
# 		for j in range( i+1, arr_size ):
# 			# if(arr[j] - arr[i] > max_diff):
# 			# 	max_diff = arr[j] - arr[i]
# 			max_diff = max(arr[j] - arr[i], max_diff)
	
# 	return max_diff
	
# arr = [110, 2, 90, 10, 1]
# print ("Original Array", arr)
# size = len(arr)
# print ("Maximum difference is", maxDiff(arr, size))

# # Time Complexity : O(n^2) 
# # Auxiliary Space : O(1)


#-----------------------------------------------------------------------------------------------------------------------


# Python3 implementation of the approach

# Function to return the maximum
# absolute difference between
# any two elements of the array


def maxAbsDiff(arr, n):

	# To store the minimum and the maximum
	# elements from the array
	minEle = arr[0]
	maxEle = arr[0]
	for i in range(1, n):
		minEle = min(minEle, arr[i])
		maxEle = max(maxEle, arr[i])

	return (maxEle - minEle)

# Driver code
arr = [110, 2, 90, 10, 1]
n = len(arr)
print(maxAbsDiff(arr, n))

# # Time Complexity : O(n)
# # Auxiliary Space : O(1)
