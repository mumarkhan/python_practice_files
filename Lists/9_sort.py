"""
    in sort()
    key= and reverse= are optional parameters
    sort()
        will sort the list in ascending order
    sort(reverse=True)
        will sort the list in descending order
    sort(key=my_func)
        will sort the list on the basis of key returned by our function
"""

l1 = [3, 1, 5, 2, 6]
print("l1 : {}".format(l1))
l1.sort()
print("After sorting l1 by sort() : {}".format(l1))

l2 = [3, 4, 2, 8, 9]
print("l2 : {}".format(l2))
l2.sort(reverse=True)
print("After sorting l2 by sort(reverse=True) : {}".format(l2))


def my_func(elem):
    return elem[0]


l3 = [(6, 2), (1, 3), (9, 4), (5, 6)]
print("l3 : {}".format(l3))
l3.sort(key=my_func)
print("After sorting l3 by sort(key=my_func) : {}".format(l3))


