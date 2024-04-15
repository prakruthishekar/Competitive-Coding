# Given a Bitonic array, find if a given ‘key’ is present in it. 
# An array is considered bitonic if it is monotonically increasing and 
# then monotonically decreasing. Monotonically increasing or decreasing
# means that for any index i in the array arr[i] != arr[i+1].

# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

# Example 1:

# Input: [1, 3, 8, 4, 3], key=4
# Output: 3
# Example 2:

# Input: [3, 8, 3, 1], key=8
# Output: 1
# Example 3:

# Input: [1, 3, 8, 12], key=12
# Output: 3



# Solution
# First, we can find the index of the maximum value of the bitonic array,
# similar to Bitonic Array Maximum. Let’s call the index of the maximum number maxIndex.

# Now, we can break the array into two sub-arrays:

# Array from index ‘0’ to maxIndex, sorted in ascending order.

# Array from index maxIndex+1 to array_length-1, sorted in descending order.

# We can then call Binary Search separately in these two arrays to search the ‘key’. 
# We can use the same Order-agnostic Binary Search for searching.






# #order agnostic binary search
# def binary_search(start, end, arr, key):
#     while start <= end:
#         mid = int (start + (end - start) / 2)
#         if key == arr [mid]:
#             return mid
#         if arr[start] < arr[end]:
#             if key < arr [mid]:
#                 end = mid - 1
#             else: # key > arr [mid]
#                 start = mid + 1
#         else: # descending order 
#             if key > arr [mid]:
#                 end = mid - 1
#             else: # key < arr [mid]
#                 start = mid + 1
#             # ascending order
#     return -1


# def search_bitonic_array(arr, key):
#     left, right = 0 , len(arr)-1

#     while (left< right):
#         mid = (left+ right)//2
#         if arr[mid] > arr[mid+1]:
#             right = mid
#         else:
#             left = mid+1
    
#     index_sub_array_1 = binary_search(0, right, arr, key)
#     if index_sub_array_1 != -1:
#             return index_sub_array_1
#     else:
#             return binary_search(right, len(arr)-1,arr, key)




# Solution 2
# You can use binary search rev and normal binary search
def binary_search(start, end,arr, target):
        while start <= end:
            mid = (start + end) // 2
            val = arr[mid]
            if val == target: return mid
            elif val > target: end = mid - 1
            else: start = mid + 1
        return -1
    
def binary_search_rev(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        val = arr[mid]
        if val == target: return mid
        elif val > target: start = mid + 1
        else: end = mid - 1
    return -1


def search_bitonic_array(arr, key):
    left, right = 0 , len(arr)-1

    while (left< right):
        mid = (left+ right)//2
        if arr[mid] > arr[mid+1]:
            right = mid
        else:
            left = mid+1
    
    index_sub_array_1 = binary_search(0, right, arr, key)
    if index_sub_array_1 != -1:
            return index_sub_array_1
    else:
            return binary_search_rev(right, len(arr)-1,arr, key)

print(search_bitonic_array([1,5,2], 2))
print(search_bitonic_array([3, 8, 3, 1], 8))
print(search_bitonic_array([1, 3, 8, 12], 12))




