def has_repeating_digits(num):
    # Convert the number to a string to easily check for repeating digits
    num_str = str(num)
    # Use a set to keep track of digits seen so far
    seen_digits = set()
    
    for digit in num_str:
        if digit in seen_digits:
            return True
        seen_digits.add(digit)
    
    return False

def countNumbers(arr):
    for n, m in arr:
        count = 0
        for num in range(n, m + 1):
            if not has_repeating_digits(num):
                count += 1
        print(count)

# Read input
# q = int(input())
# arr = []
# for _ in range(q):
#     n, m = map(int, input().split())
#     arr.append((n, m))

# # Call the function with the input
# countNumbers(arr)


# Call the function with the input
print(countNumbers([[1, 20], [9, 19]]))
# count_numbers([[7,8],[52,80],[34,84],[57,64],[74,78]])
