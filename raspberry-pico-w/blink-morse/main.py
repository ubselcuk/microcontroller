import time
from machine import Pin
led=Pin("LED", Pin.OUT)
BRate=0.25


def morse_dash():
    led.value(1)
    time.sleep(4*BRate)
    led.value(0)
    time.sleep(BRate)

def morse_pause():
    time.sleep(2*BRate)

def morse_dot():
    led.value(1)
    time.sleep(BRate)
    led.value(0)
    time.sleep(BRate)

CODE = {' ': '_', 
"'": '.----.', 
'(': '-.--.-', 
')': '-.--.-', 
',': '--..--', 
'-': '-....-', 
'.': '.-.-.-', 
'/': '-..-.', 
'0': '-----', 
'1': '.----', 
'2': '..---', 
'3': '...--', 
'4': '....-', 
'5': '.....', 
'6': '-....', 
'7': '--...', 
'8': '---..', 
'9': '----.', 
':': '---...', 
';': '-.-.-.', 
'?': '..--..', 
'A': '.-', 
'B': '-...', 
'C': '-.-.', 
'D': '-..', 
'E': '.', 
'F': '..-.', 
'G': '--.', 
'H': '....', 
'I': '..', 
'J': '.---', 
'K': '-.-', 
'L': '.-..', 
'M': '--', 
'N': '-.', 
'O': '---', 
'P': '.--.', 
'Q': '--.-', 
'R': '.-.', 
'S': '...', 
'T': '-', 
'U': '..-', 
'V': '...-', 
'W': '.--', 
'X': '-..-', 
'Y': '-.--', 
'Z': '--..', 
'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

sentence = input("Enter sentence: ")
encodedSentence = convertToMorseCode(sentence)
for i in encodedSentence:
    if i == ".":
        morse_dot()
    elif i == "-":
        morse_dash()
    else:
        morse_pause()