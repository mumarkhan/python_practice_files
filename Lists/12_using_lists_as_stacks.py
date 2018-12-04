# using lists as stack


l1 = []
for i in range(1,11):
    print("pushing : ", i)
    l1.append(i)

print("After pushing values in l1. l1 is {}".format(l1))


while len(l1) > 0:
    print("poping : ", l1.pop())

print("After poping values in l1. l1 is {}".format(l1))
