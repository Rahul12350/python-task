import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Perform calculations
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)  # num is in radians

# 3. Display the results
print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm (ln) of {num} is: {natural_log}")
print(f"Sine of {num} radians is: {sine_value}")
