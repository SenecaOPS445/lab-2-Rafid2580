#!/usr/bin/env python3


import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit(0)  # Change the exit status to 0

# Assign command line arguments to variables
name = sys.argv[1].capitalize()
age = sys.argv[2]

# Print the exact output
print("Hi " + name + ", you are " + age + " years old.")
