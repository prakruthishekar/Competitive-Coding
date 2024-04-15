# You have k lists of sorted integers in non-decreasing order. 
# Find the smallest range that includes at least one number from each of the k lists.

# We define the range [a, b] is smaller than range [c, d] 
# if b - a < d - c or a < c if b - a == d - c.

 

# Example 1:

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Example 2:

# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]


from heapq import *

def smallestRange(lists):
    min_heap = []  # min heap to track the smallest element
    current_max_num = float('-inf')  # to keep track of the largest number in the heap
    rangeStart, rangeEnd = 0, float('inf')

    for arr in (lists):
        heappush(min_heap, (arr[0], 0, arr))
        current_max_num = max(current_max_num, arr[0])

    while len(min_heap) == len(lists):
        num, i, arr = heappop(min_heap)

        if rangeEnd - rangeStart > current_max_num - num:
            rangeStart = num
            rangeEnd = current_max_num

        if len(arr) > i+1:
            # insert nect element in th heap
            heappush(min_heap, (arr[i+1], i+1 , arr))
            current_max_num = max(current_max_num, arr[i+1])

    return [rangeStart, rangeEnd]

# Example usage:
nums1 = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums2 = [[1,2,3],[1,2,3],[1,2,3]]

print(smallestRange(nums1))  
print(smallestRange(nums2)) 
