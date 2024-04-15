# Problem Statement #
# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place 
# return the new length of the array.

def removeDuplicates(arr, n):
    nextElemet = 1
    for i in range(1,len(arr)):
        if arr[nextElemet-1] != arr[i]:
            arr[nextElemet] = arr[i]
            nextElemet += 1
    # print (arr)
    return nextElemet

arr = [1, 2, 2, 2, 4, 4, 4, 5, 5]
print(removeDuplicates(arr, len(arr)))

# Time Complexity #
# The time complexity of the above algorithm will be O(N)O(N), 
# where ‘N’ is the total number of elements in the given array.

# Space Complexity #
# The algorithm runs in constant space O(1)O(1).