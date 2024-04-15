# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the 
# unsigned integer 43261596, so return 964176192 which its binary representation 
# is 00111001011110000010100101000000.

# Example 2:

# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the 
# unsigned integer 4294967293, so return 3221225471 which its binary representation 
# is 10111111111111111111111111111111.


def reverseBits( n):
        num = 0              # contains the reversed number
        for i in range(32):
            num = num << 1   # (1) shift left to have space for a new bit  
            bit = n % 2      # (2) get the rightmost bit of the input
            num += bit       # (3) add this bit to the output number 
                            #     and it will be shifted leftwards later
            n = n >> 1       # (4) drop the rightmost bit of the input
        return num



# def reverseBits( n):
#     num = bin(n)[2:].zfill(32)
#     return int(num[::-1], 2)

print(reverseBits(43261596))


# Explanation:

# bin(n) -> converts the integer no. to binary [e.g 5 to 101]. It will return a 
# string in the format '0b101' which has a prefix 0b , which stands for binary representation.
#  So, to remove 0b on the left side [2:] has been done.

# zfill(32) -> returns a copy of the string with ‘0’ characters padded to 
# the left side of the given string.

# num -> now has a string of length 32 which is a binary no.
# e.g
# num = bin(5)[2:].zfill(32)

# num is now equals to '00000000000000000000000000000101'

# int(num[::-1], 2) -> returns reverse of string num. 
# Second parameter (2) in the int() represent the base of the no.


