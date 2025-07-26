import random


def ONE_TIME_PAD(length):
    pad = []
    for _ in range(length):
        pad.append(random.randint(0, 255))
    return pad
        

def LETTER_TO_ASCII(original_message):
    ascii_message = []
    for character in original_message:
        ascii_character = ord(character)
        ascii_message.append(ascii_character) 
    return ascii_message


def ASCII_TO_BINARY(ascii_message):
    binary_message = []
    for value in ascii_message:
        binary_value = bin(value)[2:]
        while len(binary_value) < 8:
            binary_value = "0" + binary_value
        binary_message.append(binary_value)
    return binary_message


def XOR_WITH_PAD(ascii_message, pad):
    encrypted_message = []
    for i in range(len(ascii_message)):
        xor_value = ascii_message[i] ^ pad[i]
        encrypted_message.append(xor_value)
    return encrypted_message

def ENCRYPT_TO_HEX(encrypted_message):
    hex_message = []
    for value in encrypted_message:
        hex_value = hex(value)[2:]  
        hex_value = hex_value.zfill(2)  
        hex_message.append(hex_value)
    return hex_message

original_message = input("Enter a message")

ascii_message = LETTER_TO_ASCII(original_message)
print("ASCII:", ascii_message)

pad = ONE_TIME_PAD(len(ascii_message))
hex_pad = [hex(x)[2:].zfill(2) for x in pad]
print("Hex pad:", hex_pad)

binary_message = ASCII_TO_BINARY(ascii_message)
print("Binary Message:", binary_message)

encrypted_message = XOR_WITH_PAD(ascii_message, pad)
print("Encrypted Message XOR:", encrypted_message)

hex_message = ENCRYPT_TO_HEX(encrypted_message)
print("Encrypted Message Hex:", hex_message)


    








    
