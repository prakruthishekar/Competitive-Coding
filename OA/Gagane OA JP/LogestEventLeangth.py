def longestEvenWord(sentence):
    words = sentence.split()  # Split the sentence into words
    longest_even_word = "00"  # Initialize with "00" as the default answer

    for word in words:
        if len(word) % 2 == 0 and len(word) >= len(longest_even_word):
            # If the word is even-length and longer than the current longest even word
            longest_even_word = word

    return longest_even_word

# Example usage:
sentence = "Time to write great code"
result = longestEvenWord(sentence)
print(result)  # Output: "write"



# Example usage:
sentence = "You can do it the eay you like"
sentence = "It is a pleasant day today"
sentence = "you can do it"


result = longestEvenWord(sentence)
print(result)  # Output: "Time"
