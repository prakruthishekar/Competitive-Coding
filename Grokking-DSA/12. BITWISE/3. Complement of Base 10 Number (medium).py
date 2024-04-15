# Problem Statement #
# Every non-negative integer N has a binary representation, for example, 
# 8 can be represented as “1000” in binary and 7 as “0111” in binary.

# The complement of a binary representation is the number in binary that we get when we 
# change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

# For a given positive number N in base-10, return the complement of its binary 
# representation as a base-10 integer.

# Example 1:

# Input: 8
# Output: 7
# Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.

# Example 2:

# Input: 10
# Output: 5
# Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.






def calculate_bitwise_complement(num):
        sum_ = 1 
        while num > sum_:
            sum_ = sum_ * 2 + 1 # get the values in which the bit values are equal to 1
            # 1^0 = 0^1 = 1 
            # 0^0 = 1^1 = 0
        return sum_ ^ num  

print("Bitwise complement of number - " + str(8) + " is = " ,calculate_bitwise_complement(8))  
print("Bitwise complement of number - " + str(4) + " is = " ,calculate_bitwise_complement(5)) 


# XOR Operation:

# number ^ complement = all_bits_set
# Let’s add ‘number’ on both sides:

# number ^ number ^ complement = number ^ all_bits_set
# From the above-mentioned second property:

# 0 ^ complement = number ^ all_bits_set
# From the above-mentioned third property:

# complement = number ^ all_bits_set

# Firstly, when we add the given input value and it's complement we will be getting a 
# number with only ones in it (as there will be no leading zeroes).
# Now, when we consider binary numbers that only contains ones in them, they will 
# look like 1, 3 (11), 7 (111), 15 (1111) and so on. In actual, the decimal values of them looks like

# 1 = 2^0 = 1 (in binary)
# 3 = 2 * 1 + 1
# 7 = 3 * 2 + 1
# 15 = 7 * 2 + 1
# and so on for other values.
