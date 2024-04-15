def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])


# Time Complexity: O(n^2)




# Begin by iterating through the list of items to be sorted, finding 
# the smallest element in the unsorted part of the list.

# Swap the smallest element with the first element in the unsorted part 
# of the list, effectively moving it to the beginning of the list.

# Repeat step 1 and 2 for each unsorted element until the entire list is sorted.