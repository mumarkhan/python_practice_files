# nested list comprehensions

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
# it will get one value of i form outer comprehension
# and for this solve the complete inner comprehension
trans_pose = [[row[i] for row in matrix] for i in range(3)]
print(trans_pose)

