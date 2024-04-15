# def lengthOfLastWord( s: str) -> int:
#     lenLast = 0
#     for i in range(len(s)-1, -1, -1):
#         if s[i] != ' ':
#             lenLast += 1
#         elif lenLast > 0:
#             break
#     return lenLast

def lengthOfLastWord( s: str) -> int:
    wordlist = s.split()
    if wordlist:
        return len(wordlist[-1])
    return 0

print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("Hello World")) 
print(lengthOfLastWord("a"))                

