# Author: Faith Lamah
# Date: 10/24/2025
# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    for character in sentence:
        if character.isupper() and new_sentence != "":
            new_sentence += " " + character.lower()
        else:
            new_sentence += character

    return new_sentence.strip()

# Example usage

sentence = input('Enter a sentence without any spaces (Start each word capitalized):')

new_sentence = word_separator(sentence)

print(new_sentence)