def plusOne(digits):
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = plusOne(digits[:-1])
            return digits 


print(plusOne([1,2,3]))
print(plusOne([9]))
print(plusOne([9,9]))

