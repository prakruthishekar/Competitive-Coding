# Given an unsorted array of numbers, find Kth smallest number in it.

# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

# Note: For a detailed discussion about different approaches to solve this problem, take a 
# look at Kth Smallest Number.

# Example 1:

# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
# Example 2:

# Input: [1, 5, 12, 2, 11, 5], K = 4
# Output: 5
# Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].
# Example 3:

# Input: [5, 12, 11, -1, 12], K = 3
# Output: 11
# Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

from heapq import *

def find_K_largest_elements(nums, k):
    minheap = []

    # Push the first k elements onto the heap
    for num in nums[:k]:
        heappush(minheap, -num)

    # Push the remaining elements and if they are larger than the smallest element in the heap, replace it
    for num in nums[k:]:
        if -num > minheap[0]:
            heappop(minheap)
            heappush(minheap, -num)

    # Return the heap after all elements have been processed
    return -minheap[0]

print(find_K_largest_elements([3, 1, 5, 12, 2, 11], k=3))
print(find_K_largest_elements([5, 12, 11, -1, 12], k=3))


