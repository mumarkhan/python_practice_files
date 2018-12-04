# looping technique of dictionary
knights = { ' gallahad ' : ' the pure ' , ' robin ' : ' the brave ' }

print("=====================")
print(1)
print("=====================")
for k in knights.keys():
    print(k, knights[k])

# When looping through dictionaries,
# the key and corresponding value
# can be retrieved at the same time using
# the items() method.
print("=====================")
print(2)
print("=====================")
for k,v in knights.items():
    print(k, v)

# When looping through a sequence,
# the position index and corresponding value
# can be retrieved at the same
# time using the enumerate() function.
print("=====================")
print(3)
print("=====================")
for i, v in enumerate(["Hello", "Belloe", "Cello"]):
    print(i, v)

# To loop over two or more sequences
# at the same time,
# the entries can be paired with the zip() function.
roll_nos = [1, 2, 3, 4]
names = ['sara', 'ali', 'asif', 'wasif']
print("=====================")
print(4)
print("=====================")
for roll, name in zip(roll_nos, names):
    print(roll, name)

# To loop over a sequence in reverse,
# first specify the sequence
# in a forward direction and then call the reversed()
# function.
print("=====================")
print(5)
print("=====================")
for i in reversed(range(1,11)):
    print(i)

# To loop over a sequence in sorted order,
# use the sorted() function which
# returns a new sorted list while
# leaving the source unaltered.
print("=====================")
print(6)
print("=====================")
basket = [ ' apple ' , ' orange ' , ' apple ' , ' pear ' , ' orange ' , ' banana ' ]
for i in sorted(basket):
    print(i)

print("=====================")
print("6b")
print("=====================")
basket = [ ' apple ' , ' orange ' , ' apple ' , ' pear ' , ' orange ' , ' banana ' ]
for i in sorted(set(basket)):
    print(i)


