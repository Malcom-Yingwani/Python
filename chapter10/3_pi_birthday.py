from pathlib import Path

path = Path("text_files/pi_ten_million.txt")
contents = path.read_text()

lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line
    
birthday = input("Enter your birthday, in form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first 10 million digits of pi!")
else: print("Your birthday does appear in the first 10 million digits of pi")