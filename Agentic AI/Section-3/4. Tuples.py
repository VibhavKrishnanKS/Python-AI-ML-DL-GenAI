# Even Tuples are immutable in Python
masala_spices = ("Cardamom", "Cloves", "Cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main Masala spices: {spice1}, {spice2}, {spice3}")  # Output: Main Masala spices: Cardamom, Cloves, Cinnamon

ginger_ratio, cardamom_ratio, cinnamon_ratio = (2, 1, 3)
print(f"Ratio is G:{ginger_ratio}, C:{cardamom_ratio}, C:{cinnamon_ratio}")  # Output: Ratio is G:2, C:1, C:3

ginger_ratio, cardamom_ratio = 2,1
print(f"Before swapping Ratio is G:{ginger_ratio}, C:{cardamom_ratio}")  # Output: Ratio is G:2, C:1
# Swapping values using tuple unpacking
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping Ratio is G:{ginger_ratio}, C:{cardamom_ratio}")  # Output: After swapping Ratio is G:1, C:2


# The in operator can be used to check for existence of an element in a tuple - works with Tuples
print(f"Is ginger in masala spices? {'Ginger' in masala_spices}")  # Output: Is ginger in masala spices? False
print(f"Is Cinnamon in masala spices? {'Cinnamon' in masala_spices}")  # Output: Is Cinnamon in masala spices? True