# WORKING WITH MULTIPLE FILES

from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file>"""
    
    try:
        contents = filename.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approcimate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
       
# EXAMPLE 1 
# path = Path("alice.txt")
# count_words(path)

# little_women_path = Path("text_files/little_women.txt")

# print()

# count_words(little_women_path)

# moby_dick_path = Path("text_files/moby_dick.txt")

# print()
# count_words(moby_dick_path)

# EXAMPLE 2
filenames = ['alice.txt', 'siddhartha.txt', 'text_files/moby_dick.txt',
 'text_files/little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

# Use "pass" in the except block to fail silently