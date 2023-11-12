#!/usr/bin/python3
#A program check if the input character is vowel or not
Vowel_Characters = ('A','a','E','e','I','i','O','o','U','u')
character = input("Enter a single Character: ")
if character in Vowel_Characters:
    print("Character "+character+" is vowel character")
else:
    print("Character "+character+" is not vowel character")
