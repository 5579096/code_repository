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
 
    # Convert the input text to uppercase for case-insensitivity
    text = text.upper()
    #print(text)
 
    # Translate each character to Morse code
    morse_code_list = []

    for word in text.split():
        #print(word)
        morse_word = ''
        for char in word:
            #print("char: " + char)
            
            # Check if the character is alphabetic
            if char.isalpha():
                #print(d.get('key1'))
                morse_word +=  morse_code_dict.get(char) + " "
                
                #print("morse_word: " + morse_word)
                #morse_code_list.append(morse_code_dict[char])
                #print(morse_code_list)
        
        morse_code_list.append(morse_word)
        #print(morse_code_list)


        #morse_list = " / ".join(morse_word)
        #print(morse_list)

        
        # Join Morse codes for characters and use forward slash for words
        morse_result = " / ".join(morse_code_list)
 


    return morse_result
 
 
# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
print(morse_translator("Morse! Code"))