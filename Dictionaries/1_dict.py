"""
dictionaries are indexed by keys, which can be any immutable type; strings
and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples;
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
"""

dict_1 = {
    "a": "America",
    "b": "Belgium",
    "c": "Canada",
    "d": "Denmark",
    "e": "England",
    "f": "France",
    "g": "Germany"
}

print(dict_1)
# .keys() on a dictionary returns a list of all the keys used in the dictionary,
#  in arbitrary
# 2 To check whether a single key is in the
# order (if you want it sorted, just use sorted(d.keys()) instead
print("Printing keys of dict: ", dict_1.keys())
print("Printing keys of dict in sorted order: ", sorted(dict_1.keys()))


# checking key is in dict
print("is 'a' is the key in dict:", 'a' in dict_1)

# accessing specific value using key
print("dict_1['a'] =", dict_1['a'])

# deleting key from dict
del dict_1['g']
print("After deletion: ", dict_1)

# building dict from list tuples
dict_2 = dict([('w', 'work'), ('n', 'naughty')])
print("Printing dict_2=", dict_2)

# dict comprehensions
dict_3 = {(x, x**2) for x in range(1, 11)}
print("Printing dict_3=", dict_3)

# building dict using keyword arguments
dict_4 = dict(a='all', b='ball')
print("Printing dict_4=", dict_4)

