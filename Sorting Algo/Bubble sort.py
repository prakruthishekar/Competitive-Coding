def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])


# Time Complexity: O(n^2)


# Begin by iterating through the list of items to be sorted, 
# comparing each pair of adjacent items.

# If the current item is greater than the next item, swap them 
# so that the smaller item comes first.

# Continue iterating through the list and swapping adjacent items 
# as needed until you reach the end of the list.

# At this point, the largest item will have "bubbled up" to the end of the list.

# Repeat the above steps for the remaining unsorted items until the 
# entire list is sorted.