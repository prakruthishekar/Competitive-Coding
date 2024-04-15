def romanizer(numbers):
    # Mapping of Roman numerals
    numeral_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    
    # Convert a single number to Roman numeral
    def int_to_roman(num):
        result = ''
        for value in sorted(numeral_map.keys(), reverse=True):
            while num >= value:
                result += numeral_map[value]
                num -= value
        return result


    # Convert all numbers in the input list
    # for num in numbers:
    #     print("'" + int_to_roman(num) + "'")

    return [int_to_roman(num) for num in numbers]
# Test the function
numbers = [1, 2, 3, 4, 5]

print(romanizer(numbers))
print(romanizer([75,80,99,100,50]))

