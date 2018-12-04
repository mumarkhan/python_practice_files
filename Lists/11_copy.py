# copy() returns the deep copy of the list
l1 = [1, 2, 4, 5]
l2 = []
print("Before copy() l1 : {}".format(l1))
print("Before copy() l2 : {}".format(l2))
l2 = l1.copy()
print("After copy() l1 : {}".format(l1))
print("After copy() l2 : {}".format(l2))
l2.append("new thing")
print("After appending in l2. l1 is : {}".format(l1))
print("After appending in l2. l2 is : {}".format(l2))


