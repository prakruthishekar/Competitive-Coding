# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc”
# has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the
# anagrams of the pattern in the given string.

# Example 1:

# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are 
# "bca", "cab", and "abc".


def find_string_anagram(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1
    
    result_indces  = []
# our goal is to match all the characters from the 'char frequency' with the current windOW
# try to extend the range [window start, window end]
    for window_end in range (len(str)):
        right_char = str[window_end] 
        if right_char in char_frequency:
        # decrement the frequency of matched character
            char_frequency[right_char] -= 1 
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len (char_frequency) : # Have found an anagram
            result_indces.append(window_start)

        # shrink the window by one character
        if window_end >= len (pattern) - 1:
            left_char = str[window_start]
            window_start += 1 
            if left_char in char_frequency:
                if char_frequency[left_char]== 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result_indces



print(find_string_anagram("ppqp", "pq"))
print(find_string_anagram("abbcabc", "abc"))
