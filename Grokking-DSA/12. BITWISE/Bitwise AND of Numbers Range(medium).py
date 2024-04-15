# Given two integers left and right that represent the range [left, right], 
# return the bitwise AND of all numbers in this range, inclusive.

 

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0

def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    
    # While the left and right limits are not equal,
    while left < right:
        
        # Right shift the left limit by 1 bit.
        left >>= 1
        
        # Right shift the right limit by 1 bit.
        right >>= 1
        
        # Increment the 'shift' variable by 1.
        shift += 1
    
    # Left shift the left limit by 'shift' bits and return the result.
    return left << shift

print(rangeBitwiseAnd(5, 7))
print(rangeBitwiseAnd(0, 0))
print(rangeBitwiseAnd(1, 2147483647))

