# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the 
# order of characters. No two characters may map to the same character, but a character may map 
# to itself.

def isIsomorphic( s,  t) -> bool:
        if len(s) != len(t):
            return False
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t)) 

# def isIsomorphic( s,  t) -> bool:
#         dicS = {}
#         dicT = {}
        
#         for i in range(len(s)):
#             if s[i] not in dicS:
#                 dicS[s[i]] = [i]
#             else:
#                 dicS[s[i]].append(i)
#             if t[i] not in dicT:
#                 dicT[t[i]] = [i]
#             else:
#                 dicT[t[i]].append(i)
            
#             if dicS[s[i]] != dicT[t[i]]:
#                 return False
            
#         return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo","bar"))        