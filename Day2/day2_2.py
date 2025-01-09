from itertools import tee

# Helper function to generate consecutive pairs
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# Updated is_safe function
def is_safe(line):
    """
    Check if the line is strictly increasing or strictly decreasing
    with differences greater than 0 and less than or equal to 3.
    """
    increasing_count = 0
    decreasing_count = 0
    total_pairs = len(line) - 1

    for a, b in pairwise(line):
        if 0 < b - a <= 3:  # Strictly increasing
            increasing_count += 1
        elif 0 < a - b <= 3:  # Strictly decreasing
            decreasing_count += 1

    # Safe if all pairs satisfy one condition
    return increasing_count == total_pairs or decreasing_count == total_pairs

# Main logic for processing lines
def process_line(line):
    """
    Check if the line is safe. If not, check if removing one element makes it safe.
    """
    if is_safe(line):
        return True  # Line is already safe

    # Try removing each element and checking safety
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]  # Remove the i-th element
        if is_safe(modified_line):
            return True  # Line becomes safe by removing one element

    return False  # Line cannot be made safe

# Process all lines in the file
def process_file(filename):
    total_lines = 0
    safe_lines = 0
    line_results = []  # Store line safety information

    with open(filename, 'r') as file:
        for line in file:
            total_lines += 1
            line_data = list(map(int, line.strip().split()))  # Convert to integers
            is_line_safe = process_line(line_data)
            if is_line_safe:
                safe_lines += 1
            line_results.append((line_data, is_line_safe))

    return total_lines, safe_lines, line_results

# Example Usage
filename = 'input.txt'
total_lines, safe_lines, line_results = process_file(filename)

# Output Results

print("\nLine Results:")
for line_data, is_safe in line_results:
    status = "Safe" if is_safe else "Not Safe"
    print(f"Line: {line_data} -> {status}")
# Count total safe lines from the results
total_safe = sum(1 for _, is_safe in line_results if is_safe)

print(f"Total Safe Lines: {total_safe}")
