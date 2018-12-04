l1 = ["A", 2, 4, 6, 8, 9]
print("l1: ",l1)
del l1[0]
print("After del l1[0] l1 is ", l1)
# using : the value after given after : is not included
del l1[1:3]
print("After del l1[1:3] l1 is ", l1)
# del l1 will destroy the l1
# after this it will be non defined variable
del l1


