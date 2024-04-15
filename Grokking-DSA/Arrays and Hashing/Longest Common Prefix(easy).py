# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# def longestCommonPrefix(strs) -> str:
        # l = (zip(*strs))
        # # print(list(zip(*strs)))
        # prefix = ""
        # for i in l:
        #     if len(set(i))==1:
        #         prefix += i[0]
        #     else:
        #         break
        # return prefix



def longestCommonPrefix(strs) -> str:
        # pre = strs[0]
        pre = min(strs, key=len)
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre 

print(longestCommonPrefix(["flower","flow","flight"])) 
print(longestCommonPrefix(["dog","racecar","car"]))        
