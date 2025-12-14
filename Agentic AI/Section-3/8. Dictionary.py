# we can create a dictionary
chai_order = dict(type="Masala Chai", size="Medium", sugar_level=2)
print(f"Chai Order: {chai_order}")  # Output: Chai Order: {'type': 'Masala Chai', 'size': 'Medium', 'sugar_level': 2}

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquids"] = ["milk"]

print(f"Recipe base: {chai_recipe['base']}")  # Output: Recipe base: black tea
print(f"Recipe : {chai_recipe}")  # Output: Recipe : {'base': 'black tea', 'liquids': ['milk']}
# we try to delete the milk in the dict
del chai_recipe["liquids"]
print(f"Recipe after deleting liquids: {chai_recipe}")  # Output: Recipe after deleting liquids: {'base': 'black tea'}

# Membership testing
print(f"Is sugar in chai_order? {'sugar' in chai_order}")  # Output: Is sugar in chai_order? False

print(f"Is sugar_level in chai_order? {'sugar_level' in chai_order}")  # Output: Is sugar_level in chai_order? True

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 2}
print(f"Order details (keys): {chai_order.keys()}")  # Output: Order details (keys): dict_keys(['type', 'size', 'sugar'])
print(f"Order details (keys): {chai_order.values()}") # Output: Order details (keys): dict_values(['Ginger Chai', 'Medium', 2]) 
print(f"Order details (keys): {chai_order.items()}") # Output: Order details (keys): dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 2)])

last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")  # Output: Last item removed:
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated recipe: {chai_recipe}")  # Output: Updated recipe: {'base': 'black tea', 'cardamom': 'crushed', 'ginger': 'sliced'}

chai_size = chai_order["size"]
print(f"Chai size: {chai_size}")  # Output: Chai size: Medium

'''
# Below given is a code which throws error
chai_size = chai_order["customer_note"]
print(f"Chai size: {chai_size}")  # This will raise a KeyError because 'customer_note' does not exist in the dictionary
'''

# If so the value is not present for a safer side we can go with the below approach, if the value is available then it provides the value else it provides a default value
customer_note = chai_order.get("customer_note", "No special notes")
print(f"customer_note is: {customer_note}")  # Output: Chai size: No special notes