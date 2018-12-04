l1 = ["Ali", "Ahmad", "Asad", "Sara", "Tahir"]
print("L1: {}".format(l1))
# pop() remove the right most item from the list
# if index is not given
l1.pop()
print("After pop() L1 is: {}".format(l1))
index = 1
l1.pop(index)
print("After pop({}) L1 is: {}".format(index, l1))
