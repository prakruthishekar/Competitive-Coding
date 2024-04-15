# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', 
# and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long 
# sequences (substrings) that occur more than once in a DNA molecule. You may return 
# the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]


# def findRepeatedDnaSequences(s):
#     seen = set()
#     left = 0
#     repeats = set()
#     for right in range(9, len(s)):
#         if s[left:right + 1] not in seen:
#             seen.add(s[left:right + 1])
#         else:
#             repeats.add(s[left:right + 1])
#         left += 1
#     return list(repeats)


from collections import defaultdict

def findRepeatedDnaSequences(s: str):
    seen = defaultdict(int)
    repeats = set()
    for i in range(len(s) - 9):
        seq = s[i:i+10]
        seen[seq] += 1
        if seen[seq] > 1:
            repeats.add(seq)
    return list(repeats)

    

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))