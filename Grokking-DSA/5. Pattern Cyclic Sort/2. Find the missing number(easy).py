# We are given an array containing ‘n’ distinct numbers taken from
# the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Example 1:

# Input: [4, 0, 3, 1]
# Output: 2
# Example 2:

# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7




def find_missing_number(nums):
    # Summation
    return (len(nums)*len(nums) + len(nums)) // 2 - sum(nums)

def find_missing_number(nums):
# # Bitwise
    result = 0
    for counter,value in enumerate(nums):
        
        result ^= counter+1 # XOR result with numbers from the complete series

        result ^= value # XOR with the numbers given in num series
        
    return result


def find_missing_number(num):
    i ,n = 0, len(num)
    while(i< n): 
        j = num[i]  # find the correct index the value suppoe to go
        if(num[i] < n and num[i] != num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
        else:
            i += 1      
# find the first missing index and that will be our missing number:

    for i in range(len(num)):
        if num[i] != i:
            return i
    return n
         

print(find_missing_number([4,0,3,1]))
print(find_missing_number([8,3,5,2,4,6,0,1]))    

