# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting 
# some (can be none) of the characters without disturbing the relative positions of the remaining 
# characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


def isSubsequence(s, t):
        if(len(s) > len(t)):
            return False
        if(len(s) == 0):
            return True    
        sIterator = 0    
        for i in range(len(t)):
            if(s[sIterator] == t[i]):
                sIterator += 1
            if((sIterator != 0) and sIterator == (len(s)-1)):
                return True
        return False  

print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("abc","ahbgdc")) 
print(isSubsequence("b","c"))         