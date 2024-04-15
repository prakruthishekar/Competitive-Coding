
# Topics
# Companies
# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]


def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        res = []
        for i in words:
            wordset = set(i.lower())
            if (wordset&set1 == wordset) or (wordset&set2 == wordset) or (wordset&set3 == wordset):
                res.append(i)
        return res


print(findWords(["Hello","Alaska","Dad","Peace"]))
print(findWords(["omk"]))
print(findWords(["adsdf","sfd"]))
