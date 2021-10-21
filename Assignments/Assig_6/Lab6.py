## CS 101 Lab
## Program #6
## Name: Jeffrey Driskill
## Email: jtdgz8@umkc.edu

## PROBLEM:
## A Caeser Cipher encrypter/decrypter must be made using multiple functions. The user must be able
## to enter the amount of places the letters will shift and which letters/strings they want shifted.

import string 

def Encrypt(string_text, int_key)->str:     
    '''encrypt brief text input.''' 
    letters = string.ascii_uppercase
    result = ''
    for i in range(len(string_text)):
        char = string_text[i]
        if char in letters:
            result += chr(ord(char) + int_key)
        else:
            result += char
    return result

def Decrypt(string_text, int_key)->str:   
    ''' decrypts the brief tex input. ''' 
    letters = string.ascii_uppercase
    translated = ''
    for i in string_text:
        if i in letters:
            translated += chr(ord(i) - int_key)
        else:
            translated += i
    return translated

def Get_input()->str:   
    '''Requests user interaction with UI menu'''
    Print_menu()
    number = input('Enter your selection ==> ').upper()
    return number

def Print_menu():  
    '''Adds a UI for user to utilize for navigation '''
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

    
def main():   
    Again = True   
    while Again:     
        Choice = Get_input() 
        while Choice != '1' and Choice != '2' and Choice != 'Q':
            print('Error: must be 1, 2, or Q')
            Choice = Get_input()     
        if Choice == '1':      
            Plaintext = input("Enter (brief) text to encrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Ciphertext = Encrypt(Plaintext, Key)      
            print("Encrypted:", Ciphertext)     
        elif Choice == '2':       
            Ciphertext = input("Enter (brief) text to decrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Plaintext = Decrypt(Ciphertext, Key)      
            print("Decrypted:", Plaintext)
        else:       
            print("Have an ordinary day.")       
            Again = False


# our entire program: 
main() 