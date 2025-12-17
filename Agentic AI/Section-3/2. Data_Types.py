# There is a difference on how the (/) and (//) works in python
milk_litres = 7
servings = 4    
milk_per_serving = milk_litres / servings
print(f"Milk per serving (using /) : {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot (using //) : {bags_per_pot}")

# From the above code, we can see that the (/) operator performs floating-point division, resulting in a float value, while the (//) operator performs floor division, resulting in an integer value when both operands are integers.

# There is a concept in python called upcasting
# In the below example, the True value gets converted into integer 1 while performing addition
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total Actions : {total_actions}, Type of Total Actions : {type(total_actions)}")
print(f"Boolean value of Total Actions : {bool(total_actions)}")

milk_present = 0 # no milk
print(f"Is milk present? : {bool(milk_present)}")

milk_present = None # no milk
print(f"Is milk present? : {bool(milk_present)}")
