# Given two integers a and b, return the sum of the two integers without 
# using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5


# def getSum(a, b) :
#         if(a == 0): 
#             return b
#         if(b == 0): 
#             return a

#         carry = 0
        
#         while(b != 0):
#             # // If both bits are 1, we set the bit to the left (<<1) to 1 -- this is the carry step
#             carry = (a & b) << 1            
#             # // If both bits are 1, this will give us 0 (we will have a carry from the step above)
#             # // If only 1 bit is 1, this will give us 1 (there is nothing to carry)
#             a = a ^ b
#             b = carry
    
#         return a



## To satisfy Edge condition
def getSum(a, b) :
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, 
        # so to prevent overflow and stop running into infinite loop, we use 32bit mask to 
        # limit int size to 32bit )
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
            # for overflow condition like
            # -1
            #  1    
        return (a & mask) if b > 0 else a 



# def getSum(a,b):      
#     return sum([a, b])


print(getSum(-1,1))
print(getSum(5,0))   
print(getSum(5,3))        


    