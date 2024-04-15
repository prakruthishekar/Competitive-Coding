# Problem Statement #
# In a non-empty array of numbers, every number appears exactly twice except
#  two numbers that appear only once. Find the two numbers that appear only once.

# Example 1:

# Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
# Output: [4, 6]
# Example 2:

# Input: [2, 1, 3, 2]
# Output: [1, 3]



def two_single(arr):
    # Step 1: XOR all the numbers in the array
    xor_result = 0
    for num in arr:
        xor_result ^= num

    # Step 2: Find any set bit in the XOR result
    # We choose the rightmost set bit for simplicity
    rightmost_set_bit = xor_result & -xor_result
    n1 = []
    n2 = []
    # Step 3: Divide the numbers into two groups based on the chosen bit
    num1 = num2 = 0
    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num
            n1.append(num)
        else:
            num2 ^= num
            n2.append(num)

    return [num1, num2]

print(two_single([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
print(two_single([2, 1, 1 ,2,3])) 