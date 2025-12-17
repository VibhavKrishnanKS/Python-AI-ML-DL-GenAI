# Data Types

# Note - 
# 1. Everything is Object(can be Mutable (or) Immutable) in Python
# 2. Object - An object must have the below things
# 2.1 It should have an identity
# 2.1.1 Mutable Data Types - Can be changed after creation
# 2.1.2 Immutable Data Types - Cannot be changed after creation
# 2.2 It should have a type
# 2.3 It should have a value (Don't look at mutabiltiy and immutability based on value)

sugar_amount = 2
print(f"Initial Sugar Amount : {sugar_amount}")

sugar_amount = 12
print(f"Initial Sugar Amount : {sugar_amount}")

print(f"ID of 2:{id(2)}")
print(f"ID of 12:{id(12)}")

# Collection - Set
spice_mix = set()
print(spice_mix)
print(f"Initial Spice Mix : {id(spice_mix)}")
spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(spice_mix)
print(f"Spice Mix after additions : {id(spice_mix)}")
for item in spice_mix:
    print(f"Item: {item}, ID: {id(item)}")


# Note
# The id of the sugar_amount variable changes when it is reassigned to a new value, which shows that integers are immutable in Python.
# The id of the spice_mix set remains the same even after adding elements to it, which shows that sets are mutable.

# OUTPUT 1
# Initial Sugar Amount : 2
# Initial Sugar Amount : 12
# ID of 2:140707051948504
# ID of 12:140707051948824
# set()
# Initial Spice Mix : 2371450117632
# {'Cardamom', 'Ginger'}
# Spice Mix after additions : 2371450117632
# Item: Cardamom, ID: 2371450281136
# Item: Ginger, ID: 2371450290848

# OUTPUT 2
# Initial Sugar Amount : 2
# Initial Sugar Amount : 12
# ID of 2:140707051948504
# ID of 12:140707051948824
# set()
# Initial Spice Mix : 2632027151872
# {'Ginger', 'Cardamom'}
# Spice Mix after additions : 2632027151872
# Item: Ginger, ID: 2632027325088
# Item: Cardamom, ID: 2632027315376

# As you can see from the above output, the ID of the integers are the same if we run the program twice
# Whereas if we run the program twice, the ID of the set and its elements are different each time.