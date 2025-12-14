# Regarding the case of set, everything is going to be unique. - By default it is know for uniqueness only

essential_spices = { "cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices  # Union of two sets
print(f"All spices: {all_spices}")  # Output: All spices: {'cinnamon', 'cloves', 'black pepper', 'cardamom', 'ginger'}

common_spices = essential_spices & optional_spices  # Intersection of two sets
print(f"Common spices: {common_spices}")  # Output: Common spices: {'ginger'}

only_in_essential = essential_spices - optional_spices  # Difference of two sets
print(f"Spices only in essential spices: {only_in_essential}")  # Output: Spices only in essential: {'cinnamon', 'cardamom'}

print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")  # Output: Is 'cloves' in essential spices? False

print(f"Is 'ginger' in optional spices? {'ginger' in optional_spices}")  # Output: Is 'ginger' in optional spices? True