# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:43:40 2024

@author: iamrs
"""

nato_alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'
}

def convert_to_nato(word):
    return ' '.join([nato_alphabet[letter.upper()] for letter in word if letter.upper() in nato_alphabet])

# Example usage:
word = input("Enter a word: ")
print("NATO phonetic alphabet:", convert_to_nato(word))
