# Read file
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
    row3 = [abs(a - b) for a, b in zip(row1, row2)]

    # Print the sorted rows and their difference
    print("Sorted Row 1:", row1)
    print("Sorted Row 2:", row2)
    print("Row 3 (Sorted Row 1 - Sorted Row 2):", row3)
    print(sum(row3))
