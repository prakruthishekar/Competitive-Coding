# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A
    
    l , r = 0, len(A) - 1

    while True:
        i = (l + r) // 2   # mid of Array A
        j = half - i - 2   # number of elements to be taken from array B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i+1] if (i+1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j+1] if (j+1) < len(B) else float("infinity")
        
        # Partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            #odd
            if total % 2:
                return min(Aright, Bright)
            #even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i -1
        else:
            l = i + 1
print(findMedianSortedArrays([1,3,4,5,7,8,9], [2,3,4,5,6]))   
print(findMedianSortedArrays([1,2], [3,4]))    


# The time complexity of the findMedianSortedArrays function 
# is O(log(min(M, N))), where M and N are the lengths of the input
# arrays nums1 and nums2 respectively. This complexity arises from
# performing binary search on the shorter array.

# The space complexity is O(1) since the algorithm uses a constant
# amount of extra space to store variables and does not require additional
# data structures that scale with the input size.
