# Given an array, find the sum of all numbers between the K1’th and 
# K2’th smallest elements of that array.

# Example 1:

# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
# between 5 and 15 is 23 (11+12).
# Example 2:

# Input: [3, 5, 8, 7], and K1=1, K2=4
# Output: 12
# Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
# number (8) is 12 (5+7).

from heapq import *
from multiprocessing import heap
def sumOfElements(nums, k1, k2):
    minheap =[]

    for i in nums:
        heappush(minheap, i)    

    for i in range(k1):
        heappop(minheap)

    sum = 0

    for i in range(k2-k1-1):
        sum += minheap[i]
    
    return sum



print(sumOfElements([1, 3, 12, 5, 15, 11], k1=3, k2=6))
print(sumOfElements([3, 5, 8, 7], k1=1, k2=4))
