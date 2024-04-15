# Insertion Sort: Insertion sort is suitable for small datasets or when the 
# dataset is almost sorted. It has a worst-case time complexity of O(n^2), 
# but its best-case time complexity is O(n), which makes it efficient for 
# small or almost sorted datasets.


def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        # print(arr[i])
        # print(arr[arr_size - 1])
        # If the element is not
        # equal to largest element
        while( j >= 0 and arr[j] > current) :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current    
    return arr        

# Driver code

arr = [12, 35, 1, 10, 35, 1]
print(insertionSort(arr))


# Time Complexity: O(n log n). 
# Time required to sort the array is O(n log n).
# Auxiliary space: O(1). 
# As no extra space is required.



# Begin with the first element in the unsorted list, assuming it is already sorted.

# Pick the next unsorted element and insert it into the correct 
# position in the sorted sub-list.

# Compare the newly inserted element with the elements in the sorted 
# sub-list and move the larger elements one position up until the 
# correct position for the new element is found.

# Repeat steps 2 and 3 for each unsorted element until the entire list is sorted.