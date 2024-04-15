# Given a string s representing a valid expression, implement a basic calculator
# to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as 
# mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
    

def calculate(s: str) -> int:
    num = 0
    res = 0
    sign = 1
    stack = []
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in ["-","+"]:
            res = res + num * sign
            num = 0
            if char == "-":
                sign = -1
            else:
                sign = 1
        elif char == "(":
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif char == ")":
            res += sign * num
            res *= stack.pop()## process sign
            res += stack.pop() ##process with old value
            num = 0
    
    return res + num * sign

# T: O(N)
# S: O(N)


print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1+(4+5+2)-3)+(6+8)"))
