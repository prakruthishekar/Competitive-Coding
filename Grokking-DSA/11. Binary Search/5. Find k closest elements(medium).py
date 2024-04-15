# Given a sorted integer array arr, two integers k and x, 
# return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

def findClosestElements(arr, k: int, x: int):
        if arr[0] >= x:
            return arr[:k]
        if arr[-1] <= x:
            return arr[-k:]

        right = len(arr) - k
        left = 0
        while left < right:
            mid = (right + left) // 2
            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                left = mid + 1
            elif arr[mid] == arr[mid + k] and arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k] 

print(findClosestElements([1,2,3,4,5],4,3))
print(findClosestElements([1,1,2,2,2,2,2,2,2,2],3,1))

print(findClosestElements([1,2,3,4,5],4,-1))
