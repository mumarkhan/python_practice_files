matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
# * is to for unpacking arguments list
# it is to tell that
# don't take matrix as a single positional arugment
# rather take it as
#   [1, 2, 3, 4] ---- first argument
#   [5, 6, 7, 8] ---- second argument
#   [9, 10, 11, 12] ---- third argument
#   zip() will return the iterators of all these
#   three lists
#   list() will make list of tuples using these iterators
#   for example
#   { ( first elem from iterator 1 , first elem from iterator 2 , first elem from iterator 3) , ....
#   and so on
transpose = list(zip(*matrix))
print(transpose)

