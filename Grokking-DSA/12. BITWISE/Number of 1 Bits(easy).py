
# Write a function that takes an unsigned integer and returns the number of '1' 
# bits it has (also known as the Hamming weight).Input: n = 00000000000000000000000000001011


# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 
# has a total of three '1' bits.



def hammingWeight(n):
    num_of_1s = 0
        
    for i in range(32):
        # this will take out the right-most 1 of n 
        num_of_1s += (n & 1)  # Since AND operation only gives value 1 if the other values are 1 
        # else it returns 0, Hence doing AND operation with the Number will give the count of 1's
        #in the last digit
        
        n = n >> 1 # left shit
        
    return num_of_1s
    
    
    
    # counter = 0
    # while n:
        
    #     # this will take out the right-most 1 of n    
    #     n = n & (n-1)
        
    #     # update counter
    #     counter += 1
    
    # return counter

print(hammingWeight(3))
print(hammingWeight(2))    
print(hammingWeight(7))
print(hammingWeight(6))    

