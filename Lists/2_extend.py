# difference between append() and extend()
# is that append() adds new thing as a
# item to the list means only increases list size by 1
# while extend() adds the all the elements to the list as
# as new elements

l1 = [1,2,3,4,5]
print("L1: ", l1)
l2 = [5,6,7,8,9]
print("L2: ", l2)
l1.extend(l2)
print("After extending l1: ", l1)
