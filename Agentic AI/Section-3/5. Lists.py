# Lists are Mutable Sequences in Python
# We don't call them as Arrays because Python has a separate array module for that purpose. - but both are similar in many ways.

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")  # Adding an item to the end of the list
print(f"Ingredients after append: {ingredients}")  # Output: ['water', 'milk', 'black tea', 'sugar']
ingredients.remove("water")  # Removing an item from the list
print(f"Ingredients after remove: {ingredients}")  # Output: ['milk', 'black tea', 'sugar']

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)  # Extending the list with another list
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")  # Inserting an item at a specific index
print(f"chai after insert: {chai_ingredients}") # So what happens to the existing items? They get shifted to the right.
# Output: chai after insert: ['water', 'milk', 'black tea', 'ginger', 'cardamom']

last_added = chai_ingredients.pop()  # Removing and returning the last item
print(f"Last added spice: {last_added}")  # Output: Last added spice:

print(f"chai:{chai_ingredients}") # Output: chai:['water', 'milk', 'black tea', 'ginger']
# Reverse the list, not the whole list but the order of items in the list
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")  # Output: None because reverse() method modifies the list in place and returns None - so we have to print the chai_ingredients again
chai_ingredients.sort()  # Sorting the list in place
print(f"Sorted chai ingredients: {chai_ingredients}")  # Output: Sorted chai ingredients: ['black tea', 'ginger', 'milk', 'water']

print(max(chai_ingredients))  # Output: water - max works on strings based on lexicographical order

sugar_levels = [1, 2, 3, 4, 5]
print(f"Max sugar level: {max(sugar_levels)}")  # Output: Max sugar level: 5 
print(f"Min sugar level: {min(sugar_levels)}")  # Output: Min sugar level: 1

