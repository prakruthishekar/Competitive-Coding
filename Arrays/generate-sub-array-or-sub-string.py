# A subarray is a contiguous part of array. An array that is inside another array. 
# For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays. 
# The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). 
# In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.
# Complexity- O(n^3)

# Prints all subarrays in arr[0..n-1]

# def subArray(arr, n):
#     saverageArr = []
#     iterator = 0
#     # Pick starting point
#     for i in range(0,n):
#         # Pick ending point
#         for j in range(i,n):
#             # Print subarray between
#             # current starting
#             # and ending points
#             for k in range(i,j+1):
#                 saverageArr.append(arr[k])
#                 iterator += 1 

#             print(saverageArr)
#             saverageArr = [] 
#             iterator = 0 
#             # print ("\n",end="")
# arr = [1, 2, 3, 4, 5]
# n = len(arr)
# print ("All Non-empty Subarrays of an Array ", arr," are :")
# subArray(arr, n)

# # Time Complexity: 0(n^3)
# # Space Complexity: 0(1)


# ---------------------------------------------------------------------------------------------------------------

# EFFICIENT

def subArray(arr, n):
    for i in range(0,n):
        for j in range(i + 1, len(arr)+ 1):
            # Get all substrings of string
# Using string slicing
            # print(len(arr)+ 1)
            print(arr[i:j])

arr = [1, 2, 3]
n = len(arr)
print ("All Non-empty Subarrays of an Array ", arr," are :")
subArray(arr, n)

# Time Complexity: 0(n^2)
# Space Complexity: 0(1)