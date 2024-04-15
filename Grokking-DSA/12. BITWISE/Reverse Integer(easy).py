# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


def reverse(x: int) -> int:
    res = 0
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)
    while x:
        res = res * 10 + x % 10
        x //= 10
    if res.bit_length() > 31:
        return 0
    return res * sign

print(reverse(314))
print(reverse(-4314))
