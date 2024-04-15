# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0 
        window_start = 0
        window_end = k - 1
        for i in range(0,len(s)-1, k*2):
            size = k
            while(size > 1):
                temp = s[window_end] 
                s[window_end] =  s[window_start]
                s[window_start] = temp
                size -= 2
            window_end += k*2
            window_start += k*2
            # print(window_start + k)
            # print(len(s)-1)
            if((window_start + k ) >=  len(s)-1):
                return s
        return s    

s = [1,2,3,4,5,6,7,9]   
classObject = Solution() 
print(classObject.reverseStr(s, 3))          