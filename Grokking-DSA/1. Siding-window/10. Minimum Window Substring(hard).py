# Given a string and a pattern, find the smallest substring in the given 
# string which has all the characters of the given pattern.

# Example 1:

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:

# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:

# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.


# Solution #
# This problem follows the Sliding Window pattern and has a lot of similarities 
# with Permutation in a String with one difference. In this problem, we need to
#  find a substring having all characters of the pattern which means that the 
#  required substring can have some additional characters and doesn’t need to
#  be a permutation of the pattern. Here is how we will manage these differences:

# We will keep a running count of every matching instance of a character.
# Whenever we have matched all the characters, we will try to shrink the window 
# from the beginning, keeping track of the smallest substring that has all the 
# matching characters.We will stop the shrinking process as soon as we remove a 
# matched character from the sliding window. One thing to note here is that we could
# have redundant matching characters, e.g., we might have two ‘a’ in the sliding
# window when we only need one ‘a’. In that case, when we encounter the first ‘a’,
# we will simply shrink the window without decrementing the matched count. We will
# decrement the matched count when the second ‘a’ goes out of the window.



def find_minWindow_Substring(str, pattern):
    window_start, matched , sub_start = 0, 0, 0
    min_length = len(str) + 1
    char_frequency = {}
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

# try to extend the range [window start, window end]
    for window_end in range (len (str)):
        right_char = str[window_end] 
        if right_char in char_frequency:
        # decrement the frequency of matched character
            char_frequency[right_char] -= 1 
            if char_frequency[right_char] == 0:
                matched += 1

        # Shrink the window if we can, finish as soon as we romove a macthed character
        while matched == len (char_frequency) :
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                sub_start = window_start

            left_char = str[window_start]
            window_start += 1 
            if left_char in char_frequency:
                # Note that w ecould have  redundant matching characters, 
                # therfore we'll decrement the matched count only when a useful
                #  occurance of a macthed character is going out of the window
                if char_frequency[left_char]== 0:
                    matched -= 1
                char_frequency [left_char] += 1

    if min_length > len(str):
        return ""
    return str[sub_start: sub_start+ min_length]


print(find_minWindow_Substring("cbadec", "abc"))
print(find_minWindow_Substring("abdabca", "abc"))
print(find_minWindow_Substring("adcad", "abc"))
