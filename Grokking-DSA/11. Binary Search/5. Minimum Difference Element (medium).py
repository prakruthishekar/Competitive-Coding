# Given an array of numbers sorted in ascending order, find the element
# in the array that has the minimum difference with the given ‘key’.

# Example 1:

# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 
# Example 2:

# Input: [4, 6, 10], key = 4
# Output: 4
# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: 10
# Example 4:

# Input: [4, 6, 10], key = 17
# Output: 10





# Solution

# We can use a similar approach as discussed in Order-agnostic Binary Search.
# We will try to search for the ‘key’ in the given array. If we find the ‘key’ 
# we will return it as the minimum difference number. If we can’t find the ‘key’, 
# (at the end of the loop) we can find the differences between the ‘key’ and the
# numbers pointed out by indices start and end, as these two numbers will be closest 
# to the ‘key’. The number that gives minimum difference will be our required number.



def search_min_difference_element(arr, key: str) -> str:        
        if key < arr[0]:
             return arr[0]
        if key > arr[len(arr)-1]:
             return arr[len(arr)-1]
    
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (high+low)//2
            if  key > arr[mid]: # in binary search this would be only greater than
                low = mid+1
            
            elif key < arr[mid]:
                high = mid-1
            
            else:
                 return arr[mid]
        
        # at the end of loop 'start == end+1'
        # we are not able to find the element in the given array
        # return the elemen which is closest to the key

        if (abs(key - arr[low])) > abs((key - arr[high])):
             return arr[high]
        return arr[low]

print(search_min_difference_element([4, 6, 10],7))
print(search_min_difference_element([4, 6, 10],4))
print(search_min_difference_element([1, 3, 8, 10, 15],12))
print(search_min_difference_element([4,6,10],17))

