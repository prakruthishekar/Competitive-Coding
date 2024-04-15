# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ 
# closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

# Example 1:

# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]
# Example 2:

# Input: [2, 4, 5, 6, 9], K = 3, X = 6
# Output: [4, 5, 6]
# Example 3:

# Input: [2, 4, 5, 6, 9], K = 3, X = 10
# Output: [5, 6, 9]

def findClosestElements(arr, k: int, x: int):
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            midValue = arr[mid]
            
            print(x - arr[mid+k])
            print(midValue - x)

            if x - arr[mid+k] <= midValue - x:
                right = mid
            else:
                left = mid + 1
        
        return arr[left : left + k]

print(findClosestElements([5, 6, 7], k = 3, x = 7))
print(findClosestElements([2, 4, 5, 6, 9], k = 3, x = 6))
print(findClosestElements([2, 4, 5, 6, 9], k = 3, x = 10))
