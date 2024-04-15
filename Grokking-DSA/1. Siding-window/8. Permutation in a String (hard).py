# Given a string and a pattern, find out if the string contains 
# any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. 
# For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have 
# �
# !
# n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation 
# of the given pattern.

# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in 
# the given string as a substring.

# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation 
# of the given pattern.


def find_permutation (str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1
# our goal is to match all the characters from the 'char frequency' with the current windOW
# try to extend the range [window start, window end]
    for window_end in range (len (str)):
        right_char = str[window_end] 
        if right_char in char_frequency:
        # decrement the frequency of matched character
            char_frequency[right_char] -= 1 
            if char_frequency[right_char] == 0:
                matched += 1
        if matched == len (char_frequency) :
            return True
        # shrink the window by one character
        if window_end >= len (pattern) - 1:
            left_char = str[window_start]
            window_start += 1 
            if left_char in char_frequency:
                if char_frequency[left_char]== 0:
                    matched -= 1
                char_frequency [left_char] += 1

    return False



# def find_permutation(string : str, target_string: str) -> bool:
        
#         target_string = ''.join(sorted(target_string)) # O(n log n) time complexity
#         current_string = ''
        
#         for char in string:
            
#             # increase the window (equivalent to adding the next character to current string)
#             current_string += char
            
#             # start doing business once the window size is size of target_string
#             if len(current_string) == len(target_string):
                
#                 # sort the current string and check if it equals the target_string
#                 if ''.join(sorted(current_string)) == target_string:
#                     return True
                
#                 # shrink the window for next iteration (remove the leftmost character)
#                 current_string = current_string[1:]
        
#         # we couldn't find a permutation in the string, return False
#         return False

print(find_permutation("oidbcaf", "abc"))
print(find_permutation("odicf", "dc"))
print(find_permutation("bcdxabcdy", "bcdxabcdy"))

print(find_permutation("aaacb", "abc"))
