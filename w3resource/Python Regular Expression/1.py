'''
Write a Python program to check that a string contains only 
a certain set of characters (in this case a-z, A-Z and 0-9).
'''
from re import match


text = input()
regex_pattern = r"[\d\w]"
regex_validation = lambda string : bool(match(regex_pattern, string))

regex_validation(text)
