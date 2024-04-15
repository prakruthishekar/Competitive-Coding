# Given a string s and an integer k, return the maximum number of
# vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")  # To quickly check if a character is a vowel
    # Count vowels in the initial window
    curr_count = sum(1 for char in s[:k] if char in vowels)
    max_count = curr_count

    for i in range(1, len(s) - k + 1):
        # Subtract the count for the character leaving the window
        if s[i - 1] in vowels:
            curr_count -= 1
        # Add the count for the character entering the window
        if s[i + k - 1] in vowels:
            curr_count += 1
        # Update the max count if needed
        max_count = max(max_count, curr_count)

    return max_count

# Test cases
print(maxVowels("abciiidef", 3))  # Expected: 3
print(maxVowels("aeiou", 2))  # Expected: 2



