# # # Python program to
# # # find second largest
# # # element in an array


# # # Function to print the
# # # second largest elements


# def print2largest(arr, arr_size):

# 	# There should be atleast
# 		# two elements
# 	if (arr_size < 2):
	
# 		print(" Invalid Input ")
# 		return
	

# 	first = second = -2147483648
# 	for i in range(arr_size):
	
# 		# If current element is
# 				# smaller than first
# 		# then update both
# 				# first and second
# 		if (arr[i] > first):
		
# 			second = first
# 			first = arr[i]
		

# 		# If arr[i] is in
# 				# between first and
# 		# second then update second
# 		elif (arr[i] > second and arr[i] != first):
# 			second = arr[i]
	
# 	if (second == -2147483648):
# 		print("There is no second largest element")
# 	else:
# 		print("The second largest element is", second)


# arr = [12, 35, 1, 10, 34, 1]
# n = len(arr)
# print2largest(arr, n)

# # # Complexity Analysis:

# # # Time Complexity: O(n). 
# # # Only one traversal of the array is needed.
# # # Auxiliary space: O(1). 
# # # As no extra space is required.

# #----------------------------------------------------------------------------------------------------------

# # Python3 program to find second
# # largest element in an array

# # Function to print the
# # second largest elements
# def print2largest(arr,arr_size):

#     # There should be
#     # atleast two elements
#     if (arr_size < 2):
#         print(" Invalid Input ")
#         return

#     # Sort the array
#     arr.sort()
#     print(arr)
#     # Start from second last
#     # element as the largest
#     # element is at last
#     for i in range(arr_size-2,-1, -1):
#         print(arr[i])
#         print(arr[arr_size - 1])
#         # If the element is not
#         # equal to largest element
#         if (arr[i] != arr[arr_size - 1]) :
#             print("The second largest element is", arr[i])
#             return

#     print("There is no second largest element")

# # Driver code
# arr = [12, 35, 1, 10, 35, 1]
# n = len(arr)
# print2largest(arr, n)

# # Time Complexity: O(n log n). 
# # Time required to sort the array is O(n log n).
# # Auxiliary space: O(1). 
# # As no extra space is required.



print(sum([1,2]))