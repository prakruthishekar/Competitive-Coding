def longestCommonPrefix(strs) -> str:
        pre = min(strs, key=len)
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]    
        return pre 


print(longestCommonPrefix(["flower","flow","flight"]))