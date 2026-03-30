#! /usr/bin/env python3

import argparse

###------------- accept and parse command line arguments
# create an argument parser object 
parser = argparse.ArgumentParser(description="This script calculates the number at a given position in the \
                                 Fibonacci sequence")

# add a positional argument, in this case, the position in the Fibonacci sequence
parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

# Lines 5 thru 11 replaces: 
# prompt the user for a position in the Fibonacci sequence
# position = input("Please enter a position in the Fibonacci sequence: ")

# an optional argument for verbose ouput or not
# if 'store_true', this means assign 'True' if the optional argument is specified 
# on the command line, so the default for 'store_true' is actually false
parser.add_argument("-v","--verbose", help="Print verbose output", action='store_true')

# parse the arguments
args = parser.parse_args()

#initialize two integers
a,b = 0,1

for i in range(int(args.position)):
    a,b = b,a+b

fibonacci_number = a

if args.verbose:
    print(f"The Fibonacci number for {args.position} is {fibonacci_number}.")
else:
    print(fibonacci_number)

