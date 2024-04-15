class Solution(object):
    # def hammingWeight(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     count = 0
    #     n = str(bin(n))
    #     for i in range (len(n)):
    #         if n[i] == '1':
    #             count +=1
    #     return count


    def hammingWeight(self, n: int) -> int:
        num_of_1s = 0
        
        for i in range(32):
            
            num_of_1s += (n & 1)
            n = n >> 1 # left shit
            
        return num_of_1s

    # def hammingWeight(self, n: int) -> int:
    #     counter = 0
    #     while n:          
    #         # this will take out the right-most 1 of n    
    #         n = n & (n-1)
    #         # update counter
    #         counter += 1
        
    #     return counter

nums  = int('00000000000000000000000000001011',2) # giving binary input
classObject = Solution() 
print(classObject.hammingWeight(nums))            