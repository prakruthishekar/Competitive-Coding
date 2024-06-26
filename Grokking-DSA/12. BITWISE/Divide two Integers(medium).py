# Given two integers dividend and divisor, divide two integers without using 
# multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its 
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335 
# would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers 
# within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if 
# the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the 
# quotient is strictly less than -2^31, then return -2^31.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.


def divide(dividend: int, divisor: int) -> int:
    positive = (dividend < 0) is (divisor < 0) 
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
            curr_divisor, num_divisors = divisor, 1 
            while dividend >= curr_divisor:
                dividend -= curr_divisor
                res += num_divisors
                
                curr_divisor = curr_divisor << 1
                num_divisors = num_divisors << 1
				
    if not positive:
        res = -res
		
    return min(max(-2147483648, res), 2147483647)

print(divide(dividend = 10, divisor = 3))
print(divide(dividend = 7, divisor = -3))
