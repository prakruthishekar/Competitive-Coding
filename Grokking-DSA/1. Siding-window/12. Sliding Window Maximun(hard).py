# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from heapq import *

from heapq import heappush, heappop

def maxSlidingWindow(nums, k):
    result = []
    maxHeap = []

    for window_end in range(len(nums)):
        # Remove elements outside of the current window
        while maxHeap and maxHeap[0][1] < window_end - k + 1:
            heappop(maxHeap)

        # Push the current element into the heap
        heappush(maxHeap, (-nums[window_end], window_end))

        # If the window has reached its size, append the maximum element to the result
        if window_end >= k - 1:
            result.append(-maxHeap[0][0])

    return result




print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(maxSlidingWindow(nums = [1], k = 1))

