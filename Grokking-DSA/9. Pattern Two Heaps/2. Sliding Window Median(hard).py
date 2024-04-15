# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ 
# sized sub-arrays (or windows) of the array.

# Example 1:

# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:

# [1, 2, -1, 3, 5] -> median is 1.5
# [1, 2, -1, 3, 5] -> median is 0.5
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 4.0
# Example 2:

# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:

# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 2.0
# [1, 2, -1, 3, 5] -> median is 3.0

from collections import deque
import heapq

def medianSlidingWindow(nums, k: int):
        result = deque([])
        minheap = []
        maxheap = []
        # ----------------------------------------------------------------
        def balance():
            if (maxheap and minheap) and (maxheap[0] * -1) > minheap[0]:
                val = -1 * heapq.heappop(maxheap)
                heapq.heappush(minheap, val)
            if len(maxheap) > len(minheap) + 1:
                val = -1 * heapq.heappop(maxheap)
                heapq.heappush(minheap, val)
            if len(minheap) > len(maxheap) + 1:
                val = heapq.heappop(minheap)
                heapq.heappush(maxheap, -1 * val)
        # ----------------------------------------------------------------
        def find_median():
            if len(maxheap) > len(minheap):
                return (maxheap[0] * -1)
            if len(minheap) > len(maxheap):
                return (minheap[0])
            return ((maxheap[0] * -1) + minheap[0]) / 2
        # ----------------------------------------------------------------
        back = 0
        for front in range(len(nums)):
            heapq.heappush(maxheap, -1 * nums[front])
            balance()
            if (front - back + 1) >= k:
                median = find_median()
                result.append(median)
                if nums[back] in minheap:
                    minheap.remove(nums[back])
                    heapq.heapify(minheap)
                else:
                    maxheap.remove(-1 * nums[back])
                    heapq.heapify(maxheap)
                back += 1
        return result

                
print(medianSlidingWindow(nums=[1, 2, -1, 3, 5], k = 2))
print(medianSlidingWindow(nums=[1, 2, -1, 3, 5], k = 3))
