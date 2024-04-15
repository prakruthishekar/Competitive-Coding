from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.maxheap = []   # Store the lower half
        self.minheap = []   # Store the larger half
        

    def addNum(self, num: int) -> None:
        # maxheap length is either equal or 1 greater than minheap length
        # always store negative value for maxheap

# since python only implements minheap so inorder to work around is multiply num by -1
        heappush(self.maxheap, -num)
        
        # Convert to positive when retrieving from maxheap
        maxHeapTop = -heappop(self.maxheap)
        
        heappush(self.minheap, maxHeapTop)
        
        # Balance two heap
        if len(self.minheap) > len(self.maxheap):
            minHeapTop = heappop(self.minheap)
            heappush(self.maxheap,-minHeapTop) 

# heap push and pop operation ins O(long n) time complexity
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else:
            return -self.maxheap[0]

medianFinder = MedianFinder()
medianFinder.addNum(1)     #arr = [1]
medianFinder.addNum(2)     # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(5)
medianFinder.addNum(3)     # arr[1, 2, 3, 5]
medianFinder.addNum(4)
print(medianFinder.findMedian())
