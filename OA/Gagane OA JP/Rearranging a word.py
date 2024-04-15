def rearrangeWord(word):
    # Convert the word to a list for easier manipulation
    word = list(word)

    # Find the rightmost character that is lexicographically smaller than the character immediately to its right
    i = len(word) - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1

    # If no such character is found, return "no answer"
    if i == -1:
        return "no answer"

    # Find the smallest character to the right of x and greater than x
    j = len(word) - 1
    while word[j] <= word[i]:
        j -= 1

    # Swap x and y
    word[i], word[j] = word[j], word[i]

    # Reverse the substring to the right of the original position of x
    word[i + 1:] = reversed(word[i + 1:])

    # Convert the list back to a string and return it
    return ''.join(word)

# Example usage:
word = 'baca'
result = rearrangeWord(word)
result = rearrangeWord("xy")
result = rearrangeWord("pp")
result = rearrangeWord("hefg")



print(result)  # Output: 'baac'
