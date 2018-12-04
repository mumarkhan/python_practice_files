import re

str = "Sat, hat, mat, cat"
#[starting with these letters] ending_letters
all_str = re.findall("[Shmc]at" , str)

for i in all_str:
    print(i)
