# # METHOD 1 (Rotate one by one)  
# # Function to left rotate arr[] of size n by d*/
# def leftRotate(arr, d, n):
# 	for i in range(d):
# 		leftRotatebyOne(arr, n)

# # Function to left Rotate arr[] of size n by 1*/
# def leftRotatebyOne(arr, n):
# 	temp = arr[0]
# 	for i in range(n-1):
# 		arr[i] = arr[i + 1]
# 	arr[n-1] = temp
		

# # utility function to print an array */
# def printArray(arr, size):
# 	for i in range(size):
# 		print (arr[i], end = " ")


# # Driver program to test above functions */
# arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 2, 7)
# printArray(arr, 7)
# # print(arr)
# # Time complexity : O(n * d) 
# # Auxiliary Space : O(1)
# ---------------------------------------------------------------------------------------------------------------------------


# # Store the first d elements in a temp array

# def leftRotate(arr, d, n):
#     temp = arr[0:d]
#     # print(temp)
#     arr = arr[d:n] + temp
#     # print(arr)
#     return arr 

# arr = [1, 2, 3, 4, 5, 6, 7]
# print("Before Left Rotate ",arr)
# print("Array after d elements left Rotated ",leftRotate(arr, 2, 7))

# # Time complexity : O(n) 
# # Auxiliary Space : O(d)

# --------------------------------------------------------------------------------------------------------------------------

# # Python3 program to rotate an array by
# # d elements
# # Function to left rotate arr[] of size n by d
# def leftRotate(arr, d, n):
# 	d = d % n
# 	g_c_d = gcd(d, n)
# 	for i in range(g_c_d):
		
# 		# move i-th values of blocks
# 		temp = arr[i]
# 		j = i
# 		while 1:
# 			k = j + d
# 			if k >= n:
# 				k = k - n
# 			if k == i:
# 				break
# 			arr[j] = arr[k]
# 			j = k
# 		arr[j] = temp

# # UTILITY FUNCTIONS
# # function to print an array
# def printArray(arr, size):
# 	for i in range(size):
# 		print ("% d" % arr[i], end =" ")

# # Function to get gcd of a and b
# def gcd(a, b):
# 	if b == 0:
# 		return a
# 	else:
# 		return gcd(b, a % b)

# # Driver program to test above functions
# arr = [1, 2, 3, 4, 5, 6, 7]
# print("Before Rotation ", arr)
# n = len(arr)
# d = 2
# leftRotate(arr, d, n)
# print("After Rotation ", end= " ") 
# printArray(arr, n)


# # Time complexity : O(n) 
# # Auxiliary Space : O(1)



# --------------------------------------------------------------------------------------------------------------------------



# Reverse Algorithm

def leftRotate(arr, d, n):
    reverse(arr, 0 , d-1)
    print(arr)
    reverse(arr, d , n-1)
    print(arr)
    reverse(arr, 0 , n-1)
    print(arr)
    return arr

def reverse(arr, low , high):

    while(low < high):
    #    print(arr[high::-1])
    #    temp = arr[low]
    #    arr[low] = arr[high]
    #    arr[high] = temp
       swap(arr,low,high)
       low += 1
       high -= 1 

def swap(arr,low,high):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp
    


arr = [1, 2, 3, 4, 5, 6, 7]
print("Before Left Rotate ",arr)
print("Array after d elements left Rotated ",leftRotate(arr, 2, 7))

# Time complexity : O(n) 
# Auxiliary Space : O(1)
