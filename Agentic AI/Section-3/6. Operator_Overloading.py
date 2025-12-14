base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Full liquid mix: {full_liquid_mix}")  # Output: Full liquid mix: ['water', 'milk', 'ginger']
# Here the + operator is overloaded to perform concatenation of two lists

strong_brew = ["black tea"] * 3
print(f"Strong brew mix: {strong_brew}")  # Output: Strong brew mix: ['black tea', 'black tea', 'black tea'] 

strong_brew = ["black tea", "water"] * 2
print(f"Strong brew mix: {strong_brew}")  # Output: Strong brew mix: ['black tea', 'water', 'black tea', 'water']
strong_brew = ["black tea", "water"] * 0
print(f"Strong brew mix: {strong_brew}")  # Output: Strong brew mix: [] 
strong_brew = ["black tea", "water"] * -2
print(f"Strong brew mix: {strong_brew}")  # Output: Strong brew mix: []
strong_brew = ["black tea"] * 1 + ["water"] * 2
print(f"Strong brew mix: {strong_brew}")  # Output: Strong brew mix: ['black tea', 'water', 'water']

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace( b"CINN", b"CARD")
print(f"Bytes: {raw_spice_data}")  # Output: Bytes: bytearray(b'CINNAMON')
