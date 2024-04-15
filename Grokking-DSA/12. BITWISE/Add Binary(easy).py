# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"



def addBinary(a, b):
    result = ""
    carry = 0
    
    #reverse the string for the addition 
    a = a[::-1]
    b = b[::-1]
    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0   
        digitB = int(b[i]) if i < len(b) else 0

        # # ord is use to get value of ASCII character, 
        # # if the value of a[i] is 0 which is a string to be converted to an integer, 
        # # we can subtract the asci value with the asci value of 0 (to get the integer)
        
        # digitA = ord(a[i]) - ord('0')  if i < len(a) else 0
        # digitB = ord(b[j]) - ord('0') if i < len(b) else 0

        total = digitA + digitB + carry
        char = str((total) % 2)
        result = char + result
        carry = total // 2

    if (carry):
        result = "1" + result

    return result      
        

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))    
