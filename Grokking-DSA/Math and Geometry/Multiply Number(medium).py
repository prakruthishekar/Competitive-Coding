# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the
# inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

def multiply(num1: str, num2: str) -> str:
        #edge cases 
        if len(num1) == 0 or len(num2) == 0:
            return '0'
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        # convert to integer 
        res1, res2 = 0, 0 
        for d in num1:
            print(ord(d))
            print(ord('0'))
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))

        # get the product result 
        res = res1 * res2

        # convert to string, remember to reverse the result 
        ans = '' 
        while res:
            # here we find the ord value and finding the character values using ord
            ans = ans + (chr(ord('0') + res % 10)) 
            res //= 10 
        return ans[::-1]


print(multiply("22","3"))