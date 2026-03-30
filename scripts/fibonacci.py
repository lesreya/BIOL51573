#! /usr/bin/env python3

import argparse

# prompt the user for a position in the Fibonacci sequence
position = input("Please enter a position in the Fibonacci sequence: ")

#initialize two integers
a,b = 0,1

for i in range(int(position)):
    a,b = b,a+b

fibonacci_number = a

print(f"The Fibonacci number for {position} is {fibonacci_number}.")
