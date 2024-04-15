
def maxElement(arr, n): # Time Complexity : o(n)   

    max = arr[0]
    #  Traverse array elements from second and
    # // compare every element with current max
    for i in range(n):
        if (arr[i] > max):
            max = arr[i]
    return max

	
# Driver Code
if __name__ == '__main__':
	arr = [11, 15, 60, 8, 9, 10]
	n = len(arr)
	# Delete x from arr[]
	n = maxElement(arr, n)

	print("Largest element in an array is", n)

 



# def largest(arr, n): # using max() function
#     return max(arr)

# arr = [10, 324, 45, 90, 9808]
# n = len(arr)
 
# print(largest(arr, n))



# def largest(arr, n): # using sort() function
#     arr.sort()
#     print(arr)
#     return arr[n-1]

# arr = [10, 324, 45, 90, 9808]
# n = len(arr)
 
# print("Largest Element in an array",arr, "is ",largest(arr, n))
	
		
