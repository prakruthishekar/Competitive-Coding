# def pushZerosToEnd(arr, n): 
#     j = 0
#     for i in range(n):
#         if(arr[i] == 0):
#             i += 1
#         else:
#             arr[j] = arr[i]
#             j += 1

#     # return j
#     while j < n:
#         arr[j] = 0
#         j += 1

#     return n     

# arr = [0, 324,0,0, 45, 90, 9808]
# n = len(arr)
# print("Array befor pushing all zeros to end of array:")
# print(arr)
# k = pushZerosToEnd(arr, n)
# print("Array befor pushing all zeros to end of array:")
# for i in range((k)):
#     print(arr[i], end= " ")


#-------------------------------------------------------------------------------------------------------------------------

# Python3 code to move all zeroes
# at the end of array

# Function which pushes all
# zeros to end of an array.
def pushZerosToEnd(arr, n):
	count = 0 # Count of non-zero elements
	
	# Traverse the array. If element
	# encountered is non-zero, then
	# replace the element at index
	# 'count' with this element
	for i in range(n):
		if arr[i] != 0:
			
			# here count is incremented
			arr[count] = arr[i]
			count+=1
	
	# Now all non-zero elements have been
	# shifted to front and 'count' is set
	# as index of first 0. Make all
	# elements 0 from count to end.
	while count < n:
		arr[count] = 0
		count += 1
		
# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
print("Array before pushing all zeros to end of array:")
print(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

# Time Complexity: O(n) where n is number of elements in input array.
# Auxiliary Space: O(1)