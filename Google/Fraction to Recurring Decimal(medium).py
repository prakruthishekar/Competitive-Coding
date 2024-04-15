# Given two integers representing the numerator and denominator of a fraction, 
# return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# If multiple answers are possible, return any of them.

# It is guaranteed that the length of the answer string is less than 104 for all 
# the given inputs.

 

# Example 1:

# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:

# Input: numerator = 4, denominator = 333
# Output: "0.(012)"


def fractionToDecimal(numerator: int, denominator: int) -> str:
    # Handle edge cases
    if numerator == 0:
        return "0"
    if denominator == 0:
        return ""

    # Initialize result and check for negative sign
    result = ""
    if (numerator < 0) ^ (denominator < 0):
        result += "-"
    numerator, denominator = abs(numerator), abs(denominator)

    # Integer part of the result
    result += str(numerator // denominator)

    # Check if there is a fractional part
    if numerator % denominator == 0:
        return result

    result += "."

    # Use a dictionary to store the position of each remainder
    remainder_dict = {}
    remainder = numerator % denominator

    # Keep adding the remainder to the result until it repeats or the remainder becomes 0
    while remainder != 0 and remainder not in remainder_dict:
        remainder_dict[remainder] = len(result)
        remainder *= 10
        result += str(remainder // denominator)
        remainder %= denominator

    # Check if there is a repeating part
    if remainder in remainder_dict:
        result = result[:remainder_dict[remainder]] + "(" + result[remainder_dict[remainder]:] + ")"

    return result

print(fractionToDecimal(numerator = 1, denominator = 2))
print(fractionToDecimal(numerator = 2, denominator = 1))
print(fractionToDecimal(numerator = 4, denominator = 333))

