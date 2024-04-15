
# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. Return the answer 
# in any order.

# A mapping of digits to letters (just like on the telephone buttons) is 
# given below. Note that 1 does not map to any letters.

def letterCombinations(digits: str):
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        return res


print(letterCombinations("23"))