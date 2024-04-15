# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

def AverageOfSubArrayOfSizeK(arr, k):
    averageArr = []
    iterator = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] # add next element
    #slide window, we don't need to slide if we'hv not hit the required size of k
        if(i >= k-1):
            averageArr.append(sum/k) # Calculate average
            # print((sum/5))
            sum -= arr[iterator] # Subtract the element going out
            iterator += 1 # slide window
    return averageArr
      
arr = [1,3,2,6,-1,4,1,8,2]
print("Original Array", arr)
k = 5
print("The average of all contiguous subarrays of size ",k ," would be ", AverageOfSubArrayOfSizeK(arr,k))

#Time Complexity : O(n)

   