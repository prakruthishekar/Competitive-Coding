
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. 
# Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

from heapq import *

class MedianFinder:
    def __init__(self):
        self.maxheap = []   # Store the lower half
        self.minheap = []   # Store the larger half
        

    def addNum(self, num: int) -> None:
        if not self.maxheap or -self.maxheap[0] >= num:
            heappush(self.maxheap, -num)
        else:
            heappush(self.minheap, num)

        # either both heap lengths will have same length or macheap will have 1 more elemnt than inheap
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap) )
        elif len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))
    
    # heap push and pop operation ins O(long n) time complexity
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else:
            return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0
