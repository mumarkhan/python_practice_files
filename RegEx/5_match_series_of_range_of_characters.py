import re

str = "Sat, hat, mat, cat"
#[from this chracter   -   to this character] ending_letters
all_str = re.findall("[h-m]at" , str)

for i in all_str:
    print(i)
