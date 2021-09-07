from collections import Counter

s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

print('Anagram') if Counter(s1) == Counter(s2) else print('Not An Anagram')