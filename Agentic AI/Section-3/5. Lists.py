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
