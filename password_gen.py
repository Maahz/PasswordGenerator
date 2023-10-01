import sys
import random
from sys import argv
import word_list

# Check that only one argument is passed
if len(argv) != 2:
    print("Usage: python passwordGen.py <length>")
    sys.exit(1)

# Check that the argument is a positive integer
if not argv[1].isdigit():
    print("Usage: python passwordGen.py <length>")
    sys.exit(1)

# Convert the argument to an integer
length = int(argv[1])

# Generata a random password of the specified length
password = ""
for i in range(length):
    while len(password) < length:
        #Pick random word from list and capitalize it, then add it to the password
        password += random.choice(word_list.common_english_nouns).capitalize()
        # There is 25% chance of adding a random digit to the password
        if random.randint(0, 3) == 0:
            password += str(random.randint(0, 9))
        
        
print(password)
