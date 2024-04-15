def countNumbers(arr):
    def has_repeating_digits(num):
        num_str = str(num)
        return len(num_str) != len(set(num_str))
    
    for n, m in arr:
        count = 0
        for num in range(n, m + 1):
            if not has_repeating_digits(num):
                count += 1
        print(count)


def countNumbers(arr):
    def count_numbers_without_repeating_digits(n, m):
        def is_unique(num):
            digit_set = set()
            while num > 0:
                digit = num % 10
                if digit in digit_set:
                    return False
                digit_set.add(digit)
                num //= 10
            return True
        
        count = 0
        for num in range(n, m + 1):
            if is_unique(num):
                count += 1
        return count

    for n, m in arr:
        unique_digit_count = count_numbers_without_repeating_digits(n, m)
        print(unique_digit_count)

# Read input
# q = int(input())
# arr = []
# for _ in range(q):
#     n, m = map(int, input().split())
#     arr.append((n, m))

# Call the function with the input
# countNumbers(arr)

# Read input
# q = int(input())
# arr = []
# for _ in range(q):
#     n, m = map(int, input().split())
#     arr.append((n, m))

# Call the function with the input
countNumbers([[1, 20], [9, 19]])
countNumbers([[7,8],[52,80],[34,84],[57,64],[74,78]])

