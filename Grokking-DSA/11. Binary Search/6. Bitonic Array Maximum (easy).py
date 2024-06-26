
# Problem Statement #
# Find the maximum value in a given Bitonic array.
# An array is considered bitonic if it is monotonically increasing
# and then monotonically decreasing. Monotonically increasing or 
# decreasing means that for any index i in the array arr[i] != arr[i+1].

# Example 1:

# Input: [1, 3, 8, 12, 4, 2]
# Output: 12
# Explanation: The maximum number in the input bitonic array is '12'.
# Example 2:

# Input: [3, 8, 3, 1]
# Output: 8
# Example 3:

# Input: [1, 3, 8, 12]
# Output: 12
# Example 4:

# Input: [10, 9, 8]
# Output: 10





# If arr[middle] > arr[middle + 1], we are in the second (descending) part of the 
# bitonic array. Therefore, our required number could either be pointed out 
# by middle or will be before middle. This means we will be doing: end = middle.

# If arr[middle] <= arr[middle + 1], we are in the first (ascending)
# part of the bitonic array. Therefore, the required number will be after middle.
# This means we will be doing: start = middle + 1.

# We can break when start == end. Due to the two points mentioned above,
# both start and end will be pointing at the maximum number of the bitonic array.



def find_max_in_bitonic_array(arr):
    start = 0
    end = len(arr)-1
    mid = start + (end - start)/2
    while start < end:
        mid = (start+ end) // 2
        if arr[mid] > arr[mid+1]:
            end = mid
        else:
            start = mid + 1

    #at the end of while loop 'start== end'
    return arr[start]


print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
print(find_max_in_bitonic_array([3, 8, 3, 1]))
print(find_max_in_bitonic_array([1, 3, 8, 12]))
print(find_max_in_bitonic_array([10, 9, 8]))


