# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside
# the square brackets is being repeated exactly k times. Note that k is
# guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no
# extra white spaces, square brackets are well-formed, etc. Furthermore,
# you may assume that the original data does not contain any digits and
# that digits are only for those repeat numbers, k. For example, there 
# will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


def decodeString(s):
    stack=[]

    for c in s:
        if c!=']':
            stack.append(c)
        else:
            res=''
            while stack[-1]!='[':
                res+=stack.pop()
            stack.pop()
            n=''
            while len(stack)!=0 and stack[-1].isdigit()==True:
                n+=stack.pop()
            stack.append(res*int(n[::-1])) # if the number is double digit we need to flip

    return ''.join([word[::-1] for word in stack])

print(decodeString("100[leetcode]"))