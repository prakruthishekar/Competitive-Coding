# Given a string paragraph and a string array of the banned words banned, 
# return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be 
# returned in lowercase.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", 
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent 
# non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.






import re

def mostCommonWord( paragraph: str, banned) -> str:
    punctuation = "!?',;."
    for punc in punctuation:
        if punc in paragraph:
            paragraph = paragraph.replace(punc," ")

    P = paragraph.lower().split()
    mc = 0

    for words in P:
        if words not in banned and P.count(words) > mc:
            mc = P.count(words)
            word = words
    
    return(word)



# Time efficient

def getSplit(s):
    result = []
    strS = ''
    for i in s.lower():
        if i not in "!?',;. ": strS += i
        else:
            if len(strS) > 0: result.append(strS)
            strS = ''
    if len(strS) > 0: result.append(strS)
    return result

def mostCommonWord(paragraph: str, banned) -> str:
    paragraph = getSplit(paragraph)
    freq = {}
    for s in paragraph:
        if s not in banned:
            if s in freq: freq[s] += 1
            else: freq[s] = 1
            
    m = max(freq.values())
    for k in freq:
        if freq[k] == m: return k

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("..Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
print(mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))


