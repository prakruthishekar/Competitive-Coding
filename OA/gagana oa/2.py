def distribute_numbers(numbers):
    if not numbers: 
        return []

    first = [numbers[0]]
    second = [numbers[1]] if len(numbers) > 1 else []

    
    def count_greater(arr, num):
        return sum(x > num for x in arr)

    for i in range(2, len(numbers)):
        count_in_first = count_greater(first, numbers[i])
        count_in_second = count_greater(second, numbers[i])

        if count_in_first > count_in_second:
            first.append(numbers[i])
        elif count_in_second > count_in_first:
            second.append(numbers[i])
        else:  # In case of a tie
            if len(first) <= len(second):
                first.append(numbers[i])
            else:
                second.append(numbers[i])

    
    return first + second

# Example usage:
numbers = [10,8,6,4,2]
result = distribute_numbers(numbers)
print(result)  # This will print the combined array after distribution.
