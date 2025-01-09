with open('input.txt', 'r') as file:
    # Read and split into two columns
    columns = [list(map(int, line.split())) for line in file]

# Transpose columns into rows
rows = list(zip(*columns))

# Convert rows back to lists and sort each row
sorted_rows = [sorted(list(row)) for row in rows]

# Calculate the difference (row1 - row2) after sorting
if len(sorted_rows) == 2:  # Ensure there are exactly two rows
    row1 = sorted_rows[0]
    row2 = sorted_rows[1]

print("Sorted Row 1:", row1)
print("Sorted Row 2:", row2)


def count_occurrences(row1, row2):
    """
    Counts how many times each element from row1 appears in row2.
    
    Args:
    - row1 (list): The first row of numbers.
    - row2 (list): The second row of numbers.

    Returns:
    - dict: A dictionary with elements from row1 as keys and their counts in row2 as values.
    """
    return {element: row2.count(element) for element in row1}

occurrences = count_occurrences(row1, row2)
weighted_sum = 0
for element, count in occurrences.items():
    print(f"{element}: {count}")
    weighted_sum += element * count  # Accumulate the weighted sum

print("Weighted Sum:", weighted_sum)


