# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

def fullJustify(words, maxWidth):
    res = []
    i = 0
    width = 0
    cur_line = []

    while i < len(words):
        cur_word = words[i]

        if width + len(cur_word) <= maxWidth:
            cur_line.append(cur_word)
            width += len(cur_word) + 1
            i += 1
        else:
            spaces = maxWidth - width + len(cur_line)
            added = 0
            j = 0
            while added < spaces:
                if j >= len(cur_line) - 1:
                    j = 0
                
                cur_line[j] += " "
                added += 1
                j += 1
            
            res.append("".join(cur_line))
            cur_line = []
            width= 0
        
    for word in range(len(cur_line) - 1):
        cur_line[word] += " "
    
    cur_line[-1] += " " * (maxWidth- width + 1)

    res.append("".join(cur_line))
    return res

print(fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
print(fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16))

# https://leetcode.com/problems/text-justification/description/