"""
Morse Code Translator Function

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space.
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters.
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
- Non-alphabetic characters (like numbers or symbols) should not be translated.
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""


"""

def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Your code goes here
    # Remember to consider both upper and lower case letters, and spaces
    # The function should return the translated Morse code string

"""



"""
# Test cases
print(
    morse_translator("HELLO WORLD")
)  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."

print(
    morse_translator("Morse Code")
)  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
"""


def morse_translator(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    }

    #empty list
    translated_text = []
    
    for word in text.split(): #Round1: Hello, Round2: World 
        #print(text.split())
        morse_word = ''
        #print(word)
        for char in word:
            #print("char in word: " + char)
            wordupper = char.upper() #Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
            #print("wordupper: " + wordupper)

            if wordupper in morse_code_dict:
                #print("char value: " + wordupper)
                morse_word += morse_code_dict[wordupper] + ' ' #The Morse code for each character should be separated by a space.
                #print(morse_word)
        
        if morse_word:
            #print("morse word" + morse_word)
            #print(type(morse_word))
            translated_text.append(morse_word.strip())

        #print(word)
    #print(translated_text)    
    return ' / '.join(translated_text)

# Example usage:
text_to_translate = "Morse Code"
result = morse_translator(text_to_translate)
print("Result: " + result)


