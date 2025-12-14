# Strings are immutable and they cannot be changed

# In indexing the last number is not inclusive
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")  # Output: Aromatic
print(f"First word: {chai_description[0:8:1]}")  # The third parameter is step size
print(f"First word: {chai_description[0:8:2]}")  # Here we are skipping every second character
print(f"First word: {chai_description[:8:]}") # If we don't mention the first parameter it is considered as 0

print(f"Last word: {chai_description[12:]}")  # Output: Bold # Also if the last parameter is not mentioned it is considered till end of string

# In order to reverse a string we can use negative step size
print(f"Reversed string: {chai_description[::-1]}")  # Output: dloB dna citomarA

lable_text = "Chai Special"
encoded_label = lable_text.encode("utf-8")  # Encoding the string to bytes
print(f"Encoded label: {encoded_label}")  # Output: b'Chai Special
decoded_label = encoded_label.decode("utf-8")  # Decoding the bytes back to string
print(f"Decoded label: {decoded_label}")  # Output: Chai Special
