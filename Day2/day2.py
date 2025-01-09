from itertools import pairwise





def is_safe(line):
    """
    Check if the line of numbers is strictly increasing or decreasing 
    with a difference less than 3 between consecutive numbers.
    """
    # Check if strictly increasing with difference < 3
    strictly_increasing = all(a < b and b - a <= 3 for a, b in pairwise(line))
    # Check if strictly decreasing with difference < 3
    strictly_decreasing = all(a > b and a - b <= 3 for a, b in pairwise(line))
    return strictly_increasing or strictly_decreasing

    
    

total_safe = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()  # Split the line by spaces
        # Convert the line elements to integers
        numbers = list(map(int, line))
        # Call the is_safe function with the numeric list
        if is_safe(numbers):
            total_safe += 1
        print(f"total save: {total_safe}")