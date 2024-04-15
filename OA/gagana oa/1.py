def solution(numbers):
    for i in range(len(numbers) - 1):
        # Check if the current number and the next one have the same parity
        if (numbers[i] % 2 == numbers[i + 1] % 2):
            return i + 1  # Return the index of the second number where the pattern breaks
    return -1  # If the loop completes, the pattern does not break

# Example usage:
# Should return 3
print(solution([1, 2, 5, 3, 6]))

# Should return -1
print(solution([1, 4, 7, 2, 5, 6]))
