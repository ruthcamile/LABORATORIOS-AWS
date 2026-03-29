# Module Lab: Caesar Cipher Program Bug #1


def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

def getMessage():
    return input("Please enter a message to encrypt: ")

def getCipherKey():
    return input("Please enter a key (whole number from 1-25): ")

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # CORREÇÃO BUG 2 - A mensagem não estava
    # sendo convertida pra maiúscula

    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)  # CORREÇÃO BUG 1

        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter

    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)  # CORREÇÃO BUG 3 -
    # na hora de descriptografar tava usando a chave normal

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)

    myMessage = getMessage()
    myCipherKey = getCipherKey()

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')  # CORREÇÃO BUG 4 - 
    # na hora de mostrar o resultado, ele imprimia a mensagem errada

runCaesarCipherProgram()

