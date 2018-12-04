# index() gives the index of given value
# index(value)
# index(value, starting_index)
# index(value, starting_index, ending_index)
l1 = ["Ali", "Ahmad", "Asad", "Sara", "Tahir", "Sara"]
print("L1: {}".format(l1))
item = "Sara"
index1 = l1.index(item)
print("Index of {} in l1 is {}".format(item, index1))
index2 = l1.index(item, index1+1)
print("Index of {} after {} in l1 is {}".format(item, index1, index2))

