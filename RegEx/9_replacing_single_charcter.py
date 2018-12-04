import re

str = """
Barceleno
Real Mariads
Liverpool
"""
print(str)

regex = re.compile("\n")
new_str = regex.sub(" ", str)
print(new_str)


# \b: for backspace
# \t: for tab
# \v: for vertical tab
# \r: for carriage return
# \f: for form feed
