#gives starting and ending indices of the matches

import re

str_ = "We need to inform him with the latest information"

for i in re.finditer("inform", str_):
	loctup = i.span()
	print(loctup)
