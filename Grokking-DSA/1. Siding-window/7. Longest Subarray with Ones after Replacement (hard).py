# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.


from array import array


class Solution(object):
    def SubarrayAferReplacingZeros(self, arr: array, k: int) -> int:
        maxOnesCount = 0
        maxLength = 0
        left = 0
        for right in range(len(arr)):
            if(arr[right] == 1):
                maxOnesCount += 1
            # print( right - left + 1 - maxOnesCount )
            if( right - left + 1 - maxOnesCount > k):
                if( arr[left] == 1):
                    maxOnesCount -= 1 
                left += 1       
            maxLength = max(maxLength, right - left + 1)
        return maxLength

classObject = Solution()
print("[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1] with k = 2 : ", classObject.SubarrayAferReplacingZeros([0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],2))
print("[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1] with k = 3 : ", classObject.SubarrayAferReplacingZeros([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3))