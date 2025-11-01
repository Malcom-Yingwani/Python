# REDING FROM A FILE

# Reading the contents of a file

from pathlib import Path
path = Path("pi_digits.txt")

# contents = path.read_text().rstrip()
# print(contents)

# ACCESSING A FILE'S LINES

# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# WORKING WITH A FILE'S CONTENTS


contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string) 
print(len(pi_string))