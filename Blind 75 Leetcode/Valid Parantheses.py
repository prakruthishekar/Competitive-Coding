# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true



class Solution:
    def isValid(self, s: str) -> bool:

        # Unique Approach

        # if len(s) == 0:
        #     return True
        
        # if n % 2 != 0:
        #     return False
            
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('{}','').replace('()','').replace('[]','')
        
        # if s == '':
        #     return True
        # else:
        #     return False



        ## Using Stack
        
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
                # print(d[stack.pop()])
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3

  
classObject = Solution()
print(classObject.isValid("()[]{}"))  
print(classObject.isValid("(]"))     
