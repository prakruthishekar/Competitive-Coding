# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example 1:

# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.
# Example 2:

# Input: [5, 12, 11, 3, 11], K = 2
# Output: [11, 5] or [11, 12] or [11, 3]
# Explanation: Only '11' appeared twice, all other numbers appeared once.

from heapq import *

def find_k_frequent(nums, k):
    freq = {}
    for i in nums:
        freq[i] = freq.get(i, 0) + 1

    minheap = []

    for num, fre in freq.items():
        heappush(minheap,(fre,num))
        if len(minheap) > k:
            heappop(minheap)

    topNumber = []

    while minheap:
        topNumber.append(heappop(minheap)[1])

    return topNumber


print(find_k_frequent([1, 3, 5, 12, 11, 12, 11], 2))
print(find_k_frequent([5, 12, 11, 3, 11], 2))
