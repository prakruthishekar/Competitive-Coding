# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.




def margeIntersection(intervals_a, intervals_b):
    i ,j , start, end = 0, 0, 0, 1
    result = []
    while i < len(intervals_a) and j < len(intervals_b):
# check if intervals overlap and itervals_a[i]'s tart time lies within the ther intervals_b[j]
        a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and intervals_a[i][start] <= intervals_b[j][end] 

# check if intervals overlap and itervals_a[j]'s tart time lies within the ther intervals_b[i]
        b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and intervals_b[j][start] <= intervals_a[i][end]

# store the intersection part
        if (a_overlaps_b or b_overlaps_a):
            result.append([max(intervals_a[i][start], intervals_b[j][start]), min(intervals_a[i][end], intervals_b[j][end])])

# move next from the intervalwhich is finishing first
        if (intervals_a[i][end] < intervals_b[j][end]):
            i += 1
        else:
            j += 1
        
    return result
print(margeIntersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]] ))
print(margeIntersection([[1, 3], [5, 7], [9, 12]], [[5, 10]] ))
