# using lists as queue

l1 = []

for i in range(1,11):
    l1.insert(0, i)
    print("Adding ",i)

print("After inserting values l1 is ", l1)

while len(l1) > 0:
    print("Removing ", l1.pop())

print("After removing values l1 is ", l1)
