#! /usr/bin/env python3

# code here
name = input('Enter your name: ')
age = input('Enter your age: ')

name = name.lower().capitalize()

print('Hello, {}. You are {} years old'.format(name, age))

print('Hello, {name}. You are {age} years old')