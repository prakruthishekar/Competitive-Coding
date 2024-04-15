# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

# Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

# Example 1:

# Input: [3, 1, 5, 12, 2, 11], K = 3
# Output: [5, 12, 11]
# Example 2:

# Input: [5, 12, 11, -1, 12], K = 3
# Output: [12, 11, 12]

from heapq import *

def find_K_largest_elements(nums, k):
    minheap = []

    # Push the first k elements onto the heap
    for num in nums[:k]:
        heappush(minheap, num)

    # Push the remaining elements and if they are larger than the smallest element in the heap, replace it
    for num in nums[k:]:
        if num > minheap[0]:
            heappop(minheap)
            heappush(minheap, num)

    # Return the heap after all elements have been processed
    return minheap

print(find_K_largest_elements([3, 1, 5, 12, 2, 11], k=3))
print(find_K_largest_elements([5, 12, 11, -1, 12], k=3))

