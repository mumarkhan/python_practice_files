# making sets (sets are unorderd collection of unique elements)
# duplicate elements will be removed automatically
set_a = set("abcdefgqwty")
set_b = set("abcdedfdfrerfg")
print("set_a:", set_a)
print("set_b:", set_b)
print("Is 'a' in the set_a: ", 'a' in set_a)
print("letters in either set_a or set_b:", set_a | set_b)
print("letters in both set_a and set_b:", set_a & set_b)
print("letters in set_a but not in set_b:", set_a - set_b)
print("letters in set_a or in set_b but not in both:", set_a ^ set_b)

