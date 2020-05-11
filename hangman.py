import random
import string

#import the words
from words import words
"""
data structures
something for ALl letters not  guessed u-->unguessed_chars
something for all correct letters -->correct_chars_guessed
something for the word          -->word_to_guess
something for the word filled in -->word_with_chars_guessed
something for lives              --> lives
something for incorrect letters guessed  --> wrong_chars_guessed
"""

#select a random word
def getvalidword(words)
   word_to_guess=random.choice(words)

   #check if that word is valid
   #check for spaces or '-'
   while '-' in word_to_guess or ' ' in word_to_guess:
      word_to_guess=random.choice(words)
   return word_to_guess.upper()


#have the user guess a character from a-z
def 

#check if that character is valid/search the string for that character


#if found add it to the 
