def morse_translator(text):
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
 
    text = text.upper() #make text to uppercase
    morse_code_list = [] #declare to empty list

    
    for word in text.split(): #loop using for split words and store in the list
        morse_word = ""  #delcare value to tring type for collecting translted morse words
        for char in word: #loop using for split char 
            if char.isalpha(): #conditional for checking is alphabet or not
                morse_word +=  morse_code_dict.get(char) + " " #collect all morse symbol for each word
        
        morse_code_list.append(morse_word) #adding morse word to new list
    
    morse_result = " / ".join(morse_code_list) #join each separated list with / 

    return morse_result

print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
print(morse_translator("Morse! Code")) # Expected output: "-- --- .-. ... . / -.-. --- -.. ."

     
 