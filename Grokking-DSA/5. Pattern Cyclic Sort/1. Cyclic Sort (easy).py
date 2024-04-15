# Problem Statement #
# We are given an array containing ‘n’ objects. Each object, when created,
#  was assigned a unique number from 1 to ‘n’ based on their creation sequence.
#   This means that the object with sequence number ‘3’ was created just before 
#   the object with sequence number ‘4’.

# Write a function to sort the objects in-place on their creation sequence number 
# in O(n)O(n) and without any extra space. For simplicity, 
# let’s assume we are passed an integer array containing only the sequence numbers, 
# though each number is actually an object.

# Example 1:

# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]
# Example 2:

# Input: [2, 6, 4, 3, 1, 5]
# Output: [1, 2, 3, 4, 5, 6]




# Solution

# To place a number (or an object in general) at its correct index, 
# we first need to find that number. If we first find a number and
# then place it at its correct place, it will take us 
# O(N^2), which is not acceptable.

# Instead, what if we iterate the array one number at a time,
# and if the current number we are iterating is not at the correct
# index, we swap it with the number at its correct index. This way 
# we will go through all numbers and place them in their correct indices,
# hence, sorting the whole array.



def cyclic_sort(num):
    i = 0

    while(i< len(num)): 
        # print(num[i])  
        j = num[i] - 1 # find the correct index the value suppoe to go
        if(num[i] != num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
        else:
            i += 1    
    return num    




print(cyclic_sort([1, 5, 6, 4, 3, 2]))    