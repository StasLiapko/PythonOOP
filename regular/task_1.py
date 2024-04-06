import re

text = " RbbrR brRrB rbrR"

pattern = r'[Rr]b+[Rr]'

matches = re.findall(pattern, text)

print(matches)