# String Reversal
# Student: Sahar Iqbal
# Date: 10/19/2024

def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage:
result = reverse_string("hello")
print(result)  # Output: "olleh"

