# Given two sorted arrays in descending order, find ‘K’ pairs with the
#  largest sum where each pair consists of numbers from both the arrays.

# Example 1:

# Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
# Output: [9, 3], [9, 6], [8, 6] 
# Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.
# Example 2:

# Input: L1=[5, 2, 1], L2=[2, -1], K=3
# Output: [5, 2], [5, -1], [2, 2] 

from heapq import *

def kpairslarges(nums1, nums2, K):

    minHeap = []

    for i in range(0, min(K, len(nums1))):
        for j in range(0, min(K, len(nums2))):
            if len(minHeap) < K:
                heappush(minHeap, (nums1[i] + nums2[j], i , j))
            else:
                if nums1[i] + nums2[j] < minHeap[0][0]:
                    break
                else:
                    heappop(minHeap)
                    heappush(minHeap, (nums1[i] + nums2[j], i , j ))

    result= []

    for num, i, j in minHeap:
        result.append([nums1[i], nums2[j]])

    return result

print(kpairslarges([9, 8, 2], [6, 3, 1], K=3))
print(kpairslarges([5, 2, 1], [2, -1], K=3))
