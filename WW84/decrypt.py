# Define a function to find the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # Invoke the ord function to translate the letter to its ASCII code 
    # Save the code to the letterCode variable
    letterCode = ord(letter.lower())
    
    # The ASCII number representation of lowercase letter 'a'
    aAscii = ord('a')

    # The number of letters in the alphabet
    alphabetSize = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    trueLetterCode = aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)
    # print(letter, aAscii, alphabetSize, trueLetterCode)

    # Convert the ASCII number to the character or letter
    decodedLetter = chr(trueLetterCode)

    # Send the decoded letter back
    return decodedLetter


print(lassoLetter('w', 13))
print("")

# Define a function to find the truth in a secret message
# Shift the letters in a word by a specified amount to discover the hidden word
def lassoWord( word, shiftAmount ):

    # This variable is updated each time another letter is decoded
    decodedWord = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lassoLetter() function is invoked with each letter and the shift amount
        # The result (decoded letter) is stored in a variable called decodedLetter
        decodedLetter = lassoLetter(letter, shiftAmount)

        # The decodedLetter value is added to the end of the decodedWord value
        decodedWord = decodedWord + decodedLetter

    # The decodedWord is sent back to the line of code that invoked the function lassoWord()
    return decodedWord

print("Code encrypted: "+lassoWord("WHY", 13))
print("Code encrypted: "+lassoWord("oskza", -18))
print("Code encrypted: "+lassoWord("ohupo", -1))
print("Code encrypted: "+lassoWord("ED", 25))
print("Code encrypted: "+lassoWord("p", -2))





# def lassoWord( word, shiftAmount ):
#     for letter in word:
#         decodedLetter = lassoLetter( letter, shiftAmount )
#         print("cifrado = "+decodedLetter)

# print(lassoWord("hello",1))