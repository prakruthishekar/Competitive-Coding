def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    result = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result += left_half[i:]
    result += right_half[j:]
    return result



arr = [5, 2, 8, 4, 7, 1, 3, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)


# O(n log n).



# Divide the unsorted list into two halves recursively until you 
# have single-element sub-lists.

# Merge the single-element sub-lists into pairs and sort each pair
# by comparing the elements and merging them into a sorted sub-list.

# Repeat step 2 for each pair of sub-lists until the entire list is sorted.




# Unsorted list: 5 3 8 4 2

# Step 1:
# Divide the list into two halves recursively:
# 5 3 8 | 4 2
# 5 3 | 8 | 4 | 2
# 5 | 3 | 8 | 4 | 2

# Step 2:
# Merge the single-element sub-lists into pairs and sort each pair:
# 3 5 | 4 8 | 2
# 3 4 5 8 | 2

# Step 3:
# Repeat step 2 for each pair of sub-lists until the entire list is sorted:
# 2 3 4 5 8

# Sorted list: 2 3 4 5 8
