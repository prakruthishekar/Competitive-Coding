from collections import Counter

def deleteProducts(ids, m):
    # Count the occurrences of each ID
    id_counts = Counter(ids)

    # Sort the ID counts in ascending order
    sorted_counts = sorted(id_counts.values())

    # Calculate the minimum number of different IDs
    min_ids = len(sorted_counts)

    # Remove IDs with the highest frequencies while m > 0
    for count in sorted_counts:
        if m >= count:
            m -= count
            min_ids -= 1
        else:
            break

    return min_ids

# Example usage
n = 4
ids = [1, 1, 5, 5]
m = 2

result = deleteProducts(ids, m)
print(result)  # Output: 1
