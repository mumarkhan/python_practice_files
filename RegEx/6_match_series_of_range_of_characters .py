import re

str = "Sat, hat, mat, cat"
# carrot ^ means except this range
# like except from 'h' to 'm'

# [from this chracter   -   to this character] ending_letters
all_str = re.findall("[^h-m]at" , str)

for i in all_str:
    print(i)
