import re

with open(r'C:\Users\Karen Guo\OneDrive - Southern Methodist University\Advent_of_code_2024\Day3\input.txt', "r") as f:
    text = f.read()


#text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Flexible regex to capture variations like mul(2,4), mul[3,7], mul(32,64], etc.
matches = re.findall(r"mul\s*[\(\[]\s*\d+\s*,\s*\d+\s*[\)\]]", text)

#print(matches)

total_sum = 0
for match in matches:
    # Extract numbers inside the parentheses or brackets
    numbers = re.findall(r"\d+", match)
    if len(numbers) == 2:
        # Multiply the two numbers and add to the total sum
        product = int(numbers[0]) * int(numbers[1])
        total_sum += product

# Display the total sum
print(total_sum)