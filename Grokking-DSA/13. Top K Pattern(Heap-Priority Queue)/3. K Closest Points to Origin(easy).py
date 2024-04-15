# Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

# Example 1:

# Input: points = [[1,2],[1,3]], K = 1
# Output: [[1,2]]
# Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
# The Euclidean distance between (1, 3) and the origin is sqrt(10).
# Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
# Example 2:

# Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
# Output: [[1, 3], [2, -1]]

import heapq


def kClosest(points, k: int):
    heap = []
    for (x, y) in points:
        dist = -(x*x + y*y)
        if len(heap) == k:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))
    
    return [(x,y) for (dist,x, y) in heap]


print(kClosest([[1,2],[1,3]], K = 1))
print(kClosest([[1, 3], [3, 4], [2, -1]], K = 2))
