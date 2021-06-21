#Caesar decipher with key values ranging between 1 and 25 as more than 25 is just repeating
import random

#Taking the input and removing spaces
def plain_text():
 plaintext = input("Enter your plain text: ").replace(" ","").lower()
 return plaintext

def cipher_text():
 ciphertext = input("Enter your cipher text: ").replace(" ","").lower()
 return ciphertext

#Input of the encryption key
def key_input():
 key = int(input("Enter the key you want to use: "))%26
 while(key==0):
  key = int(input("You Entered multiple of 26 which gives ciphertext same as plaintext, Enter another key: "))%26
 return key

#Generating ciphertext(Encryption)
def encryption(plaintext,key):
 ciphertext = ""
 for c in plaintext:
   ciphertext+=chr(((ord(c)+key-97)%26)+97)
 #print("The ciphertext is :" + ciphertext)
 return ciphertext

#Brute Forcing all the possible plaintext from ciphertext(Decryption)
def decrypt(ciphertext):
 for i in range(1,26):
    possibletext = ""
    for c in ciphertext:
        possibletext += chr((((ord(c) - i + 26)%97) % 26) + 97)
    print("Possibility "+ str(i)+" is: " + possibletext)

def main():
 print('Welcome to Caesar cipher here are the options you can perform: ')
 option = int(input('choose the option you want to perform: '))
 if(option==0):
     plaintext = plain_text()
     key = key_input()
     print(encryption(plaintext,key))
 elif(option==1):
     ciphertext = cipher_text()
     decrypt(ciphertext)


