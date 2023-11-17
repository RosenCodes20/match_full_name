import re

names = input()
my_regex = r"\b[A-Z][a-z]+ \b[A-Z][a-z]+\b"

right_names = re.findall(my_regex, names)

for name in right_names:
    print(name, end = " ")
