from collections import Counter

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print('Anagram') if Counter(s1) == Counter(s2) else print('Not An Anagram')