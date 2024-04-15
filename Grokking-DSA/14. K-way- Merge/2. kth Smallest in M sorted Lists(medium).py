# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

# Example 1:

# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
# Output: 4
# Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
# list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
# Example 2:

# Input: L1=[5, 8, 9], L2=[1, 7], K=3
# Output: 7
# Explanation: The 3rd smallest number among all the arrays is 7.

from heapq import *

def kthsmallest(lists, k):
    minheap = []

    for i in range(len(lists)):
        heappush(minheap, (lists[i][0], 0, lists[i]))

    numbercount = 0
    # number = 0
    while minheap:
        number, i, list = heappop(minheap)
        numbercount += 1
        if numbercount == k:
            break
        
        if len(list) > i+1:
            heappush(minheap,(list[i+1], i+1 , list))

    return number


print(kthsmallest([[2, 6, 8], [3, 6,7], [1, 3, 4]], k = 5))
print(kthsmallest([[5, 8, 9], [3, 6,7]], k = 5))

