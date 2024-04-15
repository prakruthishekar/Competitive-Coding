# Given an array of positive numbers and a positive number ‘k’, 
# find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].



def MaxSumOfSubArrayOfSizeK(arr, k):
    iterator = 0
    windowSum = 0
    maxSum = 0
    for i in range(len(arr)):
        windowSum += arr[i] # add next element
    #slide window, we don't need to slide if we'hv not hit the required size of k
        if(i >= k-1):
            maxSum = max(windowSum,maxSum)
            windowSum -= arr[iterator]
            iterator += 1
           
    return maxSum

arr = [2, 3, 4, 1, 5]
print("Original Array", arr)
k = 2
print("The maximum sum subarray of size ",k ," would be ", MaxSumOfSubArrayOfSizeK(arr,k))

#Time Complexity : O(n)