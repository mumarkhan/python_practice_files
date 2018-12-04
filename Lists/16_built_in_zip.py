roll_no = [1, 2, 3]
names = ['Sara', 'John', 'Peter']
# zip() will return the iterator of tuples
# tuple will be (roll_no, name)
details = zip(roll_no, names)
for i in details:
    print(i)
# building a set from iterator of tuples
details_set = set(zip(roll_no, names))
print(details_set)


