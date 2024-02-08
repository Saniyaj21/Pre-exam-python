# Define a sample string
my_string = "Hello, World!"

# Basic slicing: Extract a substring from index 7 to 11 (excluding)
substring1 = my_string[7:11]
print("Substring 1:", substring1)  # Output: "World"

# Omitting start or stop values: If you omit the start index, it defaults to the beginning.
substring2 = my_string[:5]  # Extract from the beginning to index 4 (excluding)
print("Substring 2:", substring2)  # Output: "Hello"

# If you omit the stop index, it defaults to the end.
substring3 = my_string[7:]  # Extract from index 7 to the end
print("Substring 3:", substring3)  # Output: "World!"

# Negative indices: You can use negative indices to count from the end of the string.
substring4 = my_string[-6:-1]  # Extract from index -6 to -2 (excluding)
print("Substring 4:", substring4)  # Output: "World"

# Step value: You can specify a step value to skip characters.
substring5 = my_string[::2]  # Extract every second character
print("Substring 5:", substring5)  # Output: "Hlo ol!"

# Reverse the string using a negative step value
substring6 = my_string[::-1]
print("Reversed String:", substring6)  # Output: "!dlroW ,olleH"
