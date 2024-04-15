# Given an array of integers arr and an integer k. 
# Find the least number of unique integers after removing exactly 
# k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 
# 1 and 3 will be left.


from heapq import heappop, heappush


def findLeastNumOfUniqueInts(arr, k: int) -> int:
        freq = {}

        for i in arr:
            freq[i] = freq.get(i,0) + 1

        minheap =[]

        for i, freq in freq.items():
            heappush(minheap,[freq,i])
               
        while k > 0:
            v = heappop(minheap)
            if v[0] != 1:
                v[0] -= 1              
                heappush(minheap,v)
            k -= 1  
        return len(minheap)


print(findLeastNumOfUniqueInts([5,5,4], k = 1))
print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], k = 3))

