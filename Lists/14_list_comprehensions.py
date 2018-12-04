# comprehension lists


squares = [x**2 for x in range(1, 11)]
print(squares)

coordinates = [(x, y) for x in [1, 2, 3] for y in [1, 2, 3]]
print(coordinates)

# tuple must be parenthesized
coordinates = [(x, y) for x in [1, 2, 3] for y in [1, 2, 3] if x == y]
print(coordinates)

values = [-2, -4, -5, 0, 1, 2, 3]
positives = [x for x in values if x < 0]
print(positives)

# value cube list
cubes = [("Value:" + str(x),"Cube:" + str(x**3)) for x in range(1, 11)]
print(cubes)

# calling functions while making list
weapons = ['   bomb   ', 'tank    ', 'gun       ']
new_weapons = [weapon.strip() for weapon in weapons]
print(new_weapons)

# flattening a list
double_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for item in double_list for num in item]
print(flat_list)

