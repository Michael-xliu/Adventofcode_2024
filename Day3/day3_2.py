import re

with open(r'C:\Users\Karen Guo\OneDrive - Southern Methodist University\Advent_of_code_2024\Day3\input2.txt', "r") as f:
    text = f.read()


#text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Flexible regex to capture variations like mul(2,4), mul[3,7], mul(32,64], etc.
matches = re.findall(r"do\(\)|don'?t\(\)|mul\s*[\(\[]\s*\d+\s*,\s*\d+\s*[\)\]]", text)


#print(matches)

total_sum = 0
skip_mode = False  # Track whether we should skip processing
multiply_mode = True  # Default mode: Multiply and sum

# Process each item in the matches
for match in matches:
    if "don't()" in match:
        # Enter skip mode: Stop processing until reset
        skip_mode = True
        multiply_mode = False
        continue
    elif "do()" in match:
        # Reset to multiply mode after encountering `do()`
        skip_mode = False
        multiply_mode = True
        continue

    # Process `mul(...)` if not in skip mode
    if "mul" in match and not skip_mode:
        # Extract the numbers from `mul(...)`
        numbers = re.findall(r"\d+", match)
        if len(numbers) == 2:
            product = int(numbers[0]) * int(numbers[1])
            if multiply_mode:  # Add to the sum if in multiply mode
                total_sum += product

# Print the total sum
print("Total Sum:", total_sum)